import json
import logging

import rasa.core.channels.channel
import requests
import sanic
import sanic.response


def _compose_tyntec_send_whatsapp_text_request(apikey, from_, to, text):
    return requests.Request(
        method="POST",
        url="https://api.tyntec.com/conversations/v3/messages",
        headers={
            "Accept": "application/json",
            "apikey": apikey},
        json={
            "from": from_,
            "to": to,
            "channel": "whatsapp",
            "content": {
                "contentType": "text",
                "text": text}})


def _parse_tyntec_webhook_request(body):
    try:
        id_ = body["messageId"]
        event = body["event"]
        from_ = body["from"]
        channel = body["channel"]
        content_type = body["content"]["contentType"]
        content_text = body["content"]["text"]
    except KeyError:
        raise ValueError("body not a tyntec WhatsApp text message event")

    if event != "MoMessage" or channel != "whatsapp" or content_type != "text":
        raise ValueError("body not a WhatsApp text message event")

    return _TyntecWhatsAppTextMessage(id_, from_, content_text)


class _TyntecWhatsAppTextMessage:
    def __init__(self, id_, from_, text):
        self.id = id_
        self.from_ = from_
        self.text = text


class TyntecInputChannel(rasa.core.channels.channel.InputChannel):
    def __init__(self, waba, tyntec_apikey, requests_session=None):
        if requests_session is None:
            requests_session = requests.Session()

        self.requests_session = requests_session
        self.tyntec_apikey = tyntec_apikey
        self.waba = waba

    @classmethod
    def from_credentials(cls, credentials):
        return cls(credentials["waba"], credentials["apikey"])

    @classmethod
    def name(cls):
        return "tyntec"

    def blueprint(self, on_new_message):
        custom_webhook = sanic.Blueprint("tyntec")

        @custom_webhook.route("/", methods=["GET"])
        async def health(request):
            return sanic.response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request):
            try:
                text_message = _parse_tyntec_webhook_request(request.json)
            except ValueError:
                request_json = json.dumps(request.json)
                logging.warning(f"Unsupported event skipped: {request_json}")
                return sanic.response.text(f"Unsupported event skipped: {request_json}")

            await on_new_message(
                rasa.core.channels.channel.UserMessage(
                    text_message.text,
                    TyntecOutputChannel(self.waba, self.tyntec_apikey, self.requests_session),
                    text_message.from_,
                    input_channel=self.name(),
                    message_id=text_message.id))

            return sanic.response.text("OK")

        return custom_webhook


class TyntecOutputChannel(rasa.core.channels.channel.OutputChannel):
    def __init__(self, waba, tyntec_apikey, requests_session):
        self.requests_session = requests_session
        self.tyntec_apikey = tyntec_apikey
        self.waba = waba

    @classmethod
    def name(cls):
        return "tyntec"

    async def send_text_message(self, recipient_id, text, **kwargs):
        request = _compose_tyntec_send_whatsapp_text_request(self.tyntec_apikey, self.waba, recipient_id, text)
        prepared_request = request.prepare()

        response = self.requests_session.send(prepared_request)
        response.raise_for_status()