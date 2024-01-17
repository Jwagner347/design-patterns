import string
import random
from typing import List

#given a list of gifts, you may want to show all, show just the ones not from a given person, or show only over/under a certain amount

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Gift:
    id: str
    purchaser: str
    amount: int

    def __init__(self, purchaser, amount) -> None:
        self.id = generate_id()
        self.purchaser = purchaser
        self.amount = amount

def filter_name_strategy(name: str):
    def filter_name_fn(list: List[Gift]) -> List[Gift]:
        filtered_list = list.copy()
        filtered_list = [g for g in filtered_list if g.purchaser != name]
        return filtered_list

    return filter_name_fn


def filter_greater_lesser_strategy(greater_or_lesser: str, amt: int):

    def create_filtered_gifts(list: List[Gift]) -> List[Gift]:
        filtered_list = list.copy()
        if greater_or_lesser == "greater":
            filtered_list = [g for g in filtered_list if g.amount > amt] 
        elif greater_or_lesser == "lesser":
            filtered_list = [g for g in filtered_list if g.amount < amt] 
        else:
            raise Exception(f"Invalid greater_or_lesser value. Expected 'greater' or 'lesser', got {greater_or_lesser}")
            
        return filtered_list

    return create_filtered_gifts

def show_all_strategy():
    def create_filtered_gifts(list: List[Gift]) -> List[Gift]:
        return list.copy()
    return create_filtered_gifts

class GiftBox:
    gifts: List[Gift] = []

    def create_gift(self, purchaser, amount) -> None:
        self.gifts.append(Gift(purchaser, amount))

    def show_gift(self, gift: Gift):
        print("=======================")
        print(f"gift id: {gift.id}")
        print(f"purchaser: {gift.purchaser}")
        print(f"amount: {gift.amount}")

    def show_gifts(self, show_gifts_strategy_fn):
        gift_list = show_gifts_strategy_fn(self.gifts)

        for gift in gift_list:
            self.show_gift(gift)

        if len(self.gifts) == 0:
            print("No gifts to show")
            return

app = GiftBox()

app.create_gift("Jeff", 100)
app.create_gift("Mahfam", 200)
app.create_gift("Fandogh", 500)

app.show_gifts(filter_name_strategy("Jeff"))
app.show_gifts(show_all_strategy())
app.show_gifts(filter_greater_lesser_strategy("greater", 200))


