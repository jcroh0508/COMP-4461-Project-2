# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
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

class ActionGetAvailableMeals(Action):

    def name(self) -> Text:
        return "action_get_available_meals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # TODO: Get slot restaurant and filter returned meals by restaurant

        dishes = [{"id": 1, "name": "rice"}, {"id": 2, "name": "pasta"}]
        drinks = [{"id": 1, "name": "tea"}, {"id": 2, "name": "coke"}]

        message = "Dishes:\n"
        for dish in dishes:
            message += f'({dish.get("id")}) {dish.get("name")}\n'
        for drink in drinks:
            message += f'({drink.get("id")}) {drink.get("name")}\n'

        dispatcher.utter_message(text=message)

        return []

class ActionSubmitFoodOrder(Action):

    def name(self) -> Text:
        return "action_submit_food_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # TODO: Get slot restaurant and do some verification of meal
        # TODO: Generate payment link based on payment method and set a payment link slot

        restaurant = tracker.get_slot("restaurant")
        dish = tracker.get_slot("dish")
        drink = tracker.get_slot("drink")
        payment_method = tracker.get_slot("payment_method")

        

        dispatcher.utter_message(text="Thanks. Your order has been received")

        return [SlotSet("payment_link", "TODO")]
