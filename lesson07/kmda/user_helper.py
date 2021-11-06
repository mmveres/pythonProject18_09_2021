import json
import urllib

from lesson07.kmda.user import User
from lesson07.kmda.user_list import UserList


def get_users_from_csv(filename):
    with open(filename, "r") as file_dig:
        users = list()
        title = file_dig.readline()
        for row in file_dig:
            user_elem = row.split(";")
            users.append(User(name= user_elem[0],
                                     position= user_elem[1],
                                     salary=float(user_elem[2].replace(",", ".")),
                                     total=float(user_elem[11].replace(",", "."))
                                     )
                                )
        return users

def save_users_to_json( filename, users: UserList):
    with open(filename, "w") as file_dig:
        json.dump(users.get_users_dict(),file_dig, ensure_ascii=False)

def get_users_from_json(filename):
    users = list()
    with open(filename, "r") as file_dig:
        users_json = json.load(file_dig)
        user_dict_list = users_json["users"]
        for user_dict in user_dict_list:
            users.append(User(user_dict["name"],
                              user_dict["position"],
                              float(user_dict["salary"]),
                              float(user_dict["total"])
            ))
    return users

def get_users_from_url(url):
    data = urllib.urlopen(url)
    print(data)

if __name__ == '__main__':
    get_users_from_url()