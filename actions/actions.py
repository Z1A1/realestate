# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
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
# from typing import Any, Text, Dict, List
# from databaseintegeration import DataUpdate
# #
# from rasa_sdk import Action, Tracker,FormValidationAction
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
#
# class ValidateNameForm(FormValidationAction):
#class Actionsubmit(Action):
    # def name(self) -> Text:

    #   return "action_buyhome"
    # async def run(
    #     self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    # ) -> List[Dict[Text, Any]]:
    #   DataUpdate(tracker.get_slot("country"),    
    #   tracker.get_slot("cost"),tracker.get_slot("bedrooms"),
    #   tracker.get_slot("bathrooms"),tracker.get_slot("months"),tracker.get_slot("property_type"),tracker.get_slot("email"))
    #   return()
    #from argparse import Action


# class ActionCarosousel(Action):
#     def name(self) -> Text:
#         return "action_carosules
#         "

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: