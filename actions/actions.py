# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import mysql.connector


class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_Unit_MadOPD"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        madh = tracker.get_slot("Unit_MAdhOPD")
        print(madh)
        r = "-"
        temp1 = madh.split()
        mid_pos = len(temp1) // 2
        Madhres = ' '.join(temp1[:mid_pos] + [r] + temp1[mid_pos:])
        print(Madhres)
        M=""
        try:
            M = Madhres[0].upper() + Madhres[1:9] + Madhres[9:].upper()
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == M :
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_Unit_MOIhitech"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        hite = tracker.get_slot("Unit_Hite")
        print(hite)
        r = "-"
        temp2 = hite.split()
        mid_pos1 = len(temp2) // 2
        Hiteres = ' '.join(temp2[:mid_pos1] + [r] + temp2[mid_pos1:])
        print(Hiteres)
        MOIH=""
        try:
            MOIH = Hiteres[0:3].upper() + Hiteres[3:6] + Hiteres[6].upper() + Hiteres[7:]
            print(MOIH)
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month ")
        for d in data:
            if d["branch"] == MOIH :
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitW_C(Action):
    def name(self) -> Text:
        return "action_Unit_W&C"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        viz = tracker.get_slot("W&C_unit")
        viz_re1 = viz.replace("and","&")
        Viz1_WC=""
        try:
            Viz1_WC = viz_re1[0].upper() + viz_re1[1:6] + viz_re1[6].upper() + viz_re1[7]+viz_re1[8].upper()
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == Viz1_WC :
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionNellore(Action):
    def name(self):
        return "action_Nellore_oncology"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain:Dict[Text,Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Nellore = tracker.get_slot("Nellore_Oncology_unit")
        Nellore_health = ""
        try:
            Nellore_health = Nellore[0].upper()+Nellore[1:8]+Nellore[8].upper()+Nellore[9:16]
        except:
            dispatcher.utter_message("Please enter the correct unit name or month for the unit")
        for d in data:
            if d["branch"] == Nellore_health:
                message=dispatcher.utter_message("Location:"+ d["branch"] + ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []


class ActionUnitW_C(Action):
    def name(self) -> Text:
        return "action_Nellore"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Nellore = tracker.get_slot("nellore_Unit")
        Nellore_unit=""
        try:
            Nellore_unit = Nellore[0].upper() + Nellore[1:]
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == Nellore_unit:
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitViz(Action):
    def name(self) -> Text:
        return "action_Vizag_Health"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        viz = tracker.get_slot("vizag_health_units")
        Viz_health=""
        try:
            Viz_health = viz[0].upper()+viz[1:6]+viz[6].upper()+viz[7:13]+viz[13].upper()+viz[14:]
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month for unit")
        for d in data:
            if d["branch"] == Viz_health:
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_Unit_W&C1"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        viz = tracker.get_slot("W&C_unit")
        viz_re2 = viz.replace("and" , "&")
        Viz2_WC=""
        try:
            Viz2_WC = viz_re2[0].upper() + viz_re2[1:6] + viz_re2[6].upper() + viz_re2[8] + viz_re2[10] + viz_re2[10].upper()
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == Viz2_WC :
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_Unit_MWC"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        hite = tracker.get_slot("MWC_unit")
        print(hite)
        H=""
        try:
            H = hite[0:3].upper() + hite[3] + hite[4].upper() + hite[5:]
            print(H)
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == H :
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_Unit_MVP"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        MVP = tracker.get_slot("MVP_Unit")
        print(MVP)
        VMVP=""
        try:
            VMVP = MVP[0].upper() + MVP[1:5] + MVP[5] + MVP[6:].upper()
            print(VMVP)
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == VMVP :
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []


class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_time"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        units = tracker.get_slot("units")
        print(units)
        unit=""
        try:
            unit=units[0].upper()+units[1:]
        except:
            print(dispatcher.utter_message("Please enter the correct unit name and the month and year for unit"))

        for d in data:
            if d["branch"] == unit:
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionUnitWise(Action):
    def name(self) -> Text:
        return "action_Madhunit"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        data = l["data"]["list"]
        Madh_unit = tracker.get_slot("unit_Madh")
        print(Madh_unit)
        Madh=''
        try:
            Madh=Madh_unit[0].upper()+Madh_unit[1:9]
            print(Madh)
        except:
            dispatcher.utter_message("Please enter the correct unit name and the month")
        for d in data:
            if d["branch"] == Madh:
                message=dispatcher.utter_message("Location:"+d["branch"]+ ",Total:" + d["target"]+ ",Achieved:"+d["achieved"]+",Achieved Percentage:"+d["achievedpercentage"])
                return []
        return []

class ActionStateWiseTel(Action):
    def name(self) -> Text:
        return "action_tel"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        var = (l["data"]["list"])
        ach = []
        tar = []
        achper = []
        for x in var:
            branch = (x["branch"])
            if branch == "Nizamabad" or branch == "Chandanagar" or branch == "Madhapur - OPD" or branch == "MOI - Hitech" or branch == "Karimnagar" or branch == "Madhapur" or branch == "MWC Hitech" or branch == "Sangareddy" or branch == "Zaheerabad":
                ach.append(x["achieved"])
                tar.append(x["target"])
                achper.append(x["achievedpercentage"])
        tot_tela = sum(float(tar_tot) for tar_tot in tar)
        ach_tela = sum(float(achieved) for achieved in ach)
        achper_tela = sum(float(achi_per) for achi_per in achper)
        dispatcher.utter_message("Telangana State Target: " + str(tot_tela) + ", Achieved: " + str(ach_tela) + ", Achieved Percentage: " + str(achper_tela))
        return []

class ActionStateWiseAndh(Action):
    def name(self) -> Text:
        return "action_andh"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        var = (l["data"]["list"])
        ach = []
        tar = []
        achper = []
        for x in var:
            branch = (x["branch"])
            if branch == "Srikakulam" or branch == "Kurnool" or branch == "Vizianagaram" or branch == "Vizag Health City" or branch == "Nellore" or branch == "Kakinada" or branch == "Vizag MVP" or branch == "Vizag W&C" or branch == "Nellore Oncology":
                ach.append(x["achieved"])
                tar.append(x["target"])
                achper.append(x["achievedpercentage"])
        tot_andh = sum(float(tar_tot) for tar_tot in tar)
        ach_andh = sum(float(achieved) for achieved in ach)
        achper_andh = sum(float(achi_per) for achi_per in achper)
        dispatcher.utter_message("Andhra Pradesh State Target: " + str(tot_andh) + ", Achieved: " + str(ach_andh) + ", Achieved Percentage: " + str(achper_andh))
        return []

class ActionStateWiseMaha(Action):
    def name(self) -> Text:
        return "action_maha"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        api_url = "http://65.1.253.99/mis/new-api/revenue-center-wise.php"
        time_slot = tracker.get_slot('time')
        date_slot = tracker.get_slot('date_slot')
        date1 = time_slot[0:10]
        todo = {"accesskey": "fc3276ee1e5a4024cfdf", "date": date1}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        l = response.json()
        var = (l["data"]["list"])
        ach = []
        tar = []
        achper = []
        for x in var:
            branch = (x["branch"])
            if branch == "Aurangabad" or branch == "Nashik" or branch == "Sangamner":
                ach.append(x["achieved"])
                tar.append(x["target"])
                achper.append(x["achievedpercentage"])
        tot_mah = sum(float(tar_tot) for tar_tot in tar)
        ach_mah = sum(float(achieved) for achieved in ach)
        achper_mah = sum(float(achi_per) for achi_per in achper)
        dispatcher.utter_message("Maharastra State Target: " + str(tot_mah) + ", Achieved: " + str(ach_mah) + ", Achieved Percentage: " + str(achper_mah))
        return []
# class ActionSaveConversation(Action):
#     def name(self) -> Text:
#         return "action_save_conversation"
#     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
#         conversation = tracker.events
#         l = []
#         for i in conversation:
#             if i["event"]=="action":
#                 print(i)
#                 u=i["timestamp"]
#                 l.append(u)
#         k=tuple(l)
#         print(k)
#         mydb = mysql.connector.connect(host="localhost", username="root", password="", database="revenue")
#         my_database = mydb.cursor()
#         sql = "INSERT INTO bot_session(time_stamp) values(%d)"
#         my_database.execute(sql,k)
#         mydb.commit()
#         dispatcher.utter_message("Chat saved")
#         return []
#             # u = i["timestamp"]
#             # import mysql.connector
#             # mydb=mysql.connector.connect(host="localhost" , username="root" , password="" , database="revenue")
#             # my_database=mydb.cursor()
#             # sql = "INSERT INTO bot_session(session,time_stamp) values(i,u)"
#             # my_database.execute(sql)
#             # mydb.commit()
#             # dispatcher.utter_message("Chat saved")
#             # return []


