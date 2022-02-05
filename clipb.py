import sys
import clipboard
import json


def save_data(data):
    with open("clipboard.json", "w") as f:
        f.write(json.dumps(data))


def load_data():
    try:
        with open("clipboard.json", "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if __name__ == "__main__":
    data = load_data()
    arguments = sys.argv
    if len(arguments) == 2:
        command = arguments[1]
        if command == "save":

            key = input("key: ")
            data[key] = clipboard.paste()
            save_data(data)
            print("Save operation successful")
        elif command == "load":

            key = input("key: ")
            if key in data:
                info = data[key]
                clipboard.copy(info)
                print(info)
            else:
                print("Key does not exist")
        elif command == "list":
            for key, value in data.items():
                print(f"{key} : {value}")
        elif command == "refresh":
            save_data({})
            print("Refreshed clipboard cache")
        elif command == "del":
            key = input("key: ")
            if key in data:
                del data[key]
            save_data(data)
            print("Deleted entry")

        else:
            print("Invalid command")
    else:
        print("Invalid command")
