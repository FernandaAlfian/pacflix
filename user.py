from plan import Plan
from plan import basic_plan, standard_plan, premium_plan
from plan import list_plan


class User:

    def __init__(self, username, choosen_plan, register_date):
        self.username = username
        self.current_plan = choosen_plan
        self.register_date = register_date
        self.bill = self.current_plan.price

    