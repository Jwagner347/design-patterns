from abc import abstractmethod
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

class ShowGiftStrategy:
    @abstractmethod
    def create_filtered_gifts(self, list: List[Gift]) -> List[Gift]:
        pass

class FilterNameStrategy(ShowGiftStrategy):
    name: str

    def __init__(self, name) -> None:
        self.name = name

    def create_filtered_gifts(self, list: List[Gift]) -> List[Gift]:
        filtered_list = list.copy()
        filtered_list = [g for g in filtered_list if g.purchaser != self.name]
        return filtered_list

class ShowGreaterLesserStrategy(ShowGiftStrategy):
    greater_or_lesser: str
    amt: int

    def __init__(self, greater_or_lesser, amt) -> None:
        self.greater_or_lesser = greater_or_lesser
        self.amt = amt

    def create_filtered_gifts(self, list: List[Gift]) -> List[Gift]:
        filtered_list = list.copy()
        if self.greater_or_lesser == "greater":
            filtered_list = [g for g in filtered_list if g.amount > self.amt] 
        elif self.greater_or_lesser == "lesser":
            filtered_list = [g for g in filtered_list if g.amount < self.amt] 
        else:
            raise Exception(f"Invalid greater_or_lesser value. Expected 'greater' or 'lesser', got {self.greater_or_lesser}")
            
        return filtered_list

class ShowAllStrategy(ShowGiftStrategy):
    def create_filtered_gifts(self, list: List[Gift]) -> List[Gift]:
        return list.copy() 

class GiftBox:
    gifts: List[Gift] = []

    def create_gift(self, purchaser, amount) -> None:
        self.gifts.append(Gift(purchaser, amount))

    def show_gift(self, gift: Gift):
        print("=======================")
        print(f"gift id: {gift.id}")
        print(f"purchaser: {gift.purchaser}")
        print(f"amount: {gift.amount}")

    def show_gifts(self, strategy: ShowGiftStrategy):
        gift_list = strategy.create_filtered_gifts(self.gifts)

        for gift in gift_list:
            self.show_gift(gift)

        if len(self.gifts) == 0:
            print("No gifts to show")
            return

app = GiftBox()

app.create_gift("Jeff", 100)
app.create_gift("Mahfam", 200)
app.create_gift("Fandogh", 500)

app.show_gifts(FilterNameStrategy("Jeff"))
app.show_gifts(ShowAllStrategy())
app.show_gifts(ShowGreaterLesserStrategy("greater", 200))


