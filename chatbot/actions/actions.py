# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from pdb import Restart
from typing import Any, Text, Dict, List
import random
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

dishes = [{"id": 1, "name": "rice"}, {"id": 2, "name": "pasta"}]
drinks = [{"id": 1, "name": "tea"}, {"id": 2, "name": "coke"}]


class ActionCreateAnswer(Action):
    def name(self) -> Text:
        return "action_create_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Guess a number!")

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = random.choice(numbers)

        return [SlotSet("guessing_answer", answer), SlotSet("guess", None)]


class ValidateGuess(FormValidationAction):
    def name(self) -> Text:
        return "validate_guessing_form"

    def validate_guess(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        model_answer = int(tracker.get_slot('guessing_answer'))
        user_answer = slot_value

        if(user_answer.isdigit()):
            user_answer = int(user_answer)
            if(user_answer == model_answer):
                dispatcher.utter_message(text="That is the correct answer!")
                return{'guess': slot_value}
            elif user_answer < model_answer:
                dispatcher.utter_message(text="Too low. Try again")
                return{'guess': None}
            else:
                dispatcher.utter_message(text="Too high. Try again")
                return{'guess': None}


class ActionGetAvailableMeals(Action):

    def name(self) -> Text:
        return "action_get_available_meals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # TODO: Get slot restaurant and filter returned meals by restaurant

        message = "Dishes:\n"
        for dish in dishes:
            message += f'({dish.get("id")}) {dish.get("name")}\n'

        message += "Drinks:\n"
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

        response = f"Here's what you are ordering from {restaurant}:\n"
        response += f"- Dish: {dishes[0].get('name')}\n"
        response += f"- Drink: {drinks[0].get('name')}\n"
        response += f"You're paying with {payment_method}. Pay at https://example.com/\n"
        response += f"Thanks. Your order has been received"

        dispatcher.utter_message(text=response)

        return []
