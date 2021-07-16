# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import numpy as np
from typing import Any, Text, Dict, List
from actions.sqlite_booking import query_pid, query_pnr


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionAuthenticated(Action):
    def name(self) -> Text:
        return "action_resp_input"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
           ) -> List[Dict[Text, Any]]:   
        entities = tracker.latest_message["entities"]
        print('[log] last entities',entities)

        no_pnr = tracker.get_slot("no_pnr")
        no_pid = tracker.get_slot("no_pid")
        if no_pnr is not None:
            _input = no_pnr
            _output = query_pnr(pnr=str(no_pnr))
        elif no_pid is not None:
            _input = no_pid
            _output = query_pid(pid=str(no_pid))
        else:
            _input = 'Not found'
            _output = 'Not found'

        print("[log] input: {} \noutput: {}".format(_input,_output))

        if _input is not None:
            dispatcher.utter_message(template="utter_resp_input_success"
            , input=_input, output=_output)
        else:
            dispatcher.utter_message(template="utter_resp_input_failure")
#         dispatcher.utter_message(text="Hello World!")
        return [SlotSet("no_pnr", None), SlotSet("no_pid", None)]
