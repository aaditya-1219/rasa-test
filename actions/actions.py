# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

STUDENT_DATA = {
    "Rohan": {"age": 15, "score": 85},
    "Anjali": {"age": 14, "score": 90},
    "Kailash": {"age": 16, "score": 78},
    "Arpit": {"age": 14, "score": 92},
    "Vivek": {"age": 15, "score": 88},
}

class ActionQueryStudent(Action):
    def name(self):
        return "action_query_student"

    def run(self, dispatcher, tracker, domain):
        student_name = tracker.get_slot("name")
        print(f"Extracted student name: {student_name}")
        
        if student_name in STUDENT_DATA:
            student_info = STUDENT_DATA[student_name]
            dispatcher.utter_message(text=f"{student_name} is {student_info['age']} years old with a score of {student_info['score']}.")
        else:
            dispatcher.utter_message(text=f"Sorry, I don't have information about {student_name}.")
        
        return []