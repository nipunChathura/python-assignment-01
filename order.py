import json
import os
from pprint import pprint

__db_location__ = "db/order"
__order_folder__ = f"{__db_location__}/order"
__order_detail_folder__ = f"{__db_location__}/order_detail"
__order_last_id__ = f"{__db_location__}/order_id.db"
__order_detail_last_id__ = f"{__db_location__}/order_detail_id.db"


def init():
    db()


def db():
    os.makedirs(__order_folder__)


def set_command_and_params(command, params):
    if command == "init":
        init()
    elif command == "add":
        __add_order__(*params)
        pass
    elif command == "find":
        __find_order__(*params)
        pass
    elif command == "findAll":
        __find_all_order__
        pass
    elif command == "search":
        __order_search__(*params)
        pass


def __add_order__(order_id, customer_id, total_price, order_detail_location):
    pass


def __find_all_order__():
    pass


def __find_order__(order_id):
    pass


def __order_search__(key, value):
    pass


def __add_order_details__(order_id, item_id, item_qty, item_price, total_price):
    pass


def __find_order_detail_by_order_id(order_id):
    pass


class Order:
    def __init__(self):
        self.order_detail_location = None
        self.total_price = None
        self.customerId = None
        if os.path.exists(__order_last_id__):
            with open(__order_last_id__, "r") as last_order_id_f:
                self.last_order_id = int(last_order_id_f.readline())
        else:
            self.last_order_id = 0

    def save(self):
        order_id = self.last_order_id + 1
        _data_ = {
            "orderId": order_id,
            "customerId": self.customerId,
            "totalPrice": self.total_price,
            "orderDetailLocation": self.order_detail_location
        }
        with open(f"{__order_folder__}/{order_id}.db", "w") as order_file:
            json.dump(_data_, order_file)

        self.last_order_id += 1
        with open(__order_last_id__, "w") as f:
            f.write(str(self.last_order_id))


class Detail:
    def __init__(self):
        self.item_total_price = None
        self.item_price = None
        self.item_qty = None
        self.item_id = None
        if os.path.exists(__order_detail_last_id__):
            with open(__order_detail_last_id__, "r") as last_order_detail_id_f:
                self.last_order_detail_id = int(last_order_detail_id_f.readline())

        else:
            self.last_order_detail_id = 0

    def save(self, order_id):
        order_detail_id = self.last_order_detail_id + 1
        _data_ = {
            "orderDetailsId": order_detail_id,
            "orderId": order_id,
            "itemId": self.item_id,
            "itemQty": self.item_qty,
            "itemPrice": self.item_price,
            "itemTotalPrice": self.item_total_price
        }
        with open(f"{__order_folder__}/{order_detail_id}.db", "w") as order_file:
            json.dump(_data_, order_file)

        self.last_order_detail_id += 1
        with open(__order_last_id__, "w") as f:
            f.write(str(self.last_order_detail_id))