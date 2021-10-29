from os import waitpid
import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"
__user_folder__ = f"{__db_location__}/user"
__user_last_id__ = f"{__db_location__}/user_id.db"


def init():
    db()


def db():
    os.makedirs(__user_folder__)


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def view():
    username = __get_logged_user()
    print(username)


def login(username):
    user = username
    f = open(__session_file__, "w")
    f.write(username)
    f.close


def set_command_and_params(command, params):
    if command == "init":
        init()
    elif command == "singup":
        print("User is sing up")
    elif command == "login":
        login(*params)
    elif command == "view":
        view()
