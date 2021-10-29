from os import waitpid
import json
import os
from pprint import pprint

__db_location__ = "db"
__item_folder__ = f"{__db_location__}/item"
__item_last_id__ = f"{__db_location__}/item_id.db"


def init():
    db()


def db():
    os.makedirs(__item_folder__)


def set_command_and_params(command, params):
    if command == "init":
        init()
    elif command == "create":
        __item_create__(*params)
    elif command == "find":
        pass
    elif command == "find all":
        pass
    elif command == "search":
        pass


def __item_create__(name, qty, price):
    item = Item()
    item.name = name
    item.qty = qty
    item.price = price
    print(item.name, item.qty, item.price)
    item.save()


def __item_find__(item_id):
    print("Item find")


def __item_all__():
    print("Item All")


def __item_search__(key, value):
    print("Item search")


class Item:
    def __init__(self):
        self.price = None
        self.qty = None
        self.name = None
        if os.path.exists(__item_last_id__):
            with open(__item_last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        print("save ", self.name, self.qty, self.price)
        item_id = self.last_id + 1
        print("item_id", item_id)
        _data_ = {
            "id": item_id,
            "name": self.name,
            "qty": self.qty,
            "price": self.price
        }
        print("_data_", _data_.values().__str__())
        with open(f"{__item_folder__}/{item_id}.db", "w") as item_file:
            json.dump(_data_, item_file)

        print(self.last_id)

        self.last_id += 1
        with open(__item_last_id__, "w") as f:
            f.write(str(self.last_id))
