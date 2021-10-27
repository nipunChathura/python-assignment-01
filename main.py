import sys
from item import Item

if __name__ == "__main__":
    arguments = sys.argv

    section = arguments[1]
    command = arguments[2]
    params = arguments[3:]
    print(section, command, params)

    if section == "user":
        item = Item()
        item.set_command_and_params(command, params)

