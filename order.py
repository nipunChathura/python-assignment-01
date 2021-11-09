import json
import os
from pprint import pprint
import item

__db_location__ = "db/order"
__order_folder__ = f"{__db_location__}/order"
__order_detail_folder__ = f"{__db_location__}/order_detail"
__order_last_id__ = f"{__db_location__}/order_id.db"
__order_detail_last_id__ = f"{__db_location__}/order_detail_id.db"


def init():
    db()


def db():
    os.makedirs(__order_folder__)
    os.makedirs(__order_detail_folder__)


def set_command_and_params(command, params):
    if command == "init":
        init()
    elif command == "add":
        __add_order__()
        pass
    elif command == "find":
        __find_order__(*params)
        pass
    elif command == "findAll":
        __find_all_order__()
        pass
    elif command == "search":
        __order_search__(*params)
        pass


def __add_order__():
    print("Enter order details")
    o = Order()
    o.order_id = o.last_order_id + 1
    o.customer_id = input("customer id : ")
    total_price = 0

    items = item.get_items()
    for i in items:
        details = Detail()
        status = input(i.name + " " + i.price + " plz enter add or skip item : ")
        if status == "add":
            details.order_id = o.order_id
            details.item_id = i.item_id
            details.item_price = int(i.price)
            details.item_qty = int(input("The number of items you take : "))
            details.item_total_price = int(i.price) * int(details.item_qty)
            total_price += int(details.item_total_price)
            details.save()
        else:
            pass

    o.total_price = total_price
    o.save()
    print("Success added")


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
        self.order_id = None
        self.total_price = int
        self.customer_id = None
        if os.path.exists(__order_last_id__):
            with open(__order_last_id__, "r") as last_order_id_f:
                self.last_order_id = int(last_order_id_f.readline())
        else:
            self.last_order_id = 0

    def save(self):
        _data_ = {
            "orderId": self.order_id,
            "customerId": self.customer_id,
            "totalPrice": self.total_price,
        }
        with open(f"{__order_folder__}/{self.order_id}.db", "w") as order_file:
            json.dump(_data_, order_file)

        self.last_order_id += 1
        with open(__order_last_id__, "w") as f:
            f.write(str(self.last_order_id))


class Detail:
    def __init__(self):
        self.order_id = None
        self.item_total_price = None
        self.item_price = None
        self.item_qty = None
        self.item_id = None
        if os.path.exists(__order_detail_last_id__):
            with open(__order_detail_last_id__, "r") as last_order_detail_id_f:
                self.last_order_detail_id = int(last_order_detail_id_f.readline())
        else:
            self.last_order_detail_id = 0

    def save(self):
        order_detail_id = self.last_order_detail_id + 1
        _data_ = {
            "orderDetailsId": order_detail_id,
            "orderId": self.order_id,
            "itemId": self.item_id,
            "itemQty": self.item_qty,
            "itemPrice": self.item_price,
            "itemTotalPrice": self.item_total_price
        }
        with open(f"{__order_detail_folder__}/{self.last_order_detail_id + 1}.db", "w") as order_details_file:
            json.dump(_data_, order_details_file)

        self.last_order_detail_id += 1
        with open(__order_detail_last_id__, "w") as f:
            f.write(str(self.last_order_detail_id))
