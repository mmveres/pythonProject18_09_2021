from lesson07.kmda import user_helper
from lesson07.kmda.user_list import UserList

if __name__ == '__main__':
    users = UserList(user_helper.get_users_from_file("lipen-2019.csv"))
    print(users)
    print(users.get_user_with_max_salary())
    print(users.get_user_list_with_max_salary())