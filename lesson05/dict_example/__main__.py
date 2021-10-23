import json

if __name__ == '__main__':
    users = {
        "Tom": {
            "phone": "+971478745",
            "email": "tom12@gmail.com"
        },
        "Bob": {
            "phone": "+876390444",
            "email": "bob@gmail.com",
            "skype": "bob123"
        }
    }
    for key in users.keys():
        print(key, users[key]["phone"])

    for value in users.values():
        print(value["phone"])

    print(users["Tom"]["phone"])

    users["Tom"]["telegram"]="@tom"

    print(users)

    with open("users.json", "w") as file_dig:
            json.dump(users,file_dig)

    with open("users.json", "r") as file_dig:
            users_json = json.load(file_dig)
            print(users_json)
