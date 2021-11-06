import urllib

from lesson07.kmda import user_helper
from lesson07.kmda.user_list import UserList

if __name__ == '__main__':


    users = UserList(user_helper.get_users_from_csv("lipen-2019.csv"))
    print(users)
    print(users.get_user_with_max_salary())
    print(users.get_user_list_with_max_salary())
    for user in users.get_users():
        print(user.to_dict())

    print(users.get_users_dict())
    user_helper.save_users_to_json("users.json",users)

    print(user_helper.get_users_from_json("users.json"))