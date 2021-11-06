class UserList:
    def __init__(self, users = list()):
        self.__users = users


    def get_users(self):
        return self.__users

    def get_users_dict(self):
        users_dict =dict()
        users_dict["users"] = list()
        for user in self.__users:
            users_dict["users"].append(user.to_dict())
        return users_dict

    def get_user_with_max_salary(self):
        max_salary_user = self.__users[0]
        for user in self.__users:
            if max_salary_user.salary < user.salary:
                max_salary_user = user
        return max_salary_user

    def get_user_list_with_max_salary(self):
        user_list = list()
        max_salary_user = self.__users[0]
        for user in self.__users:
            if max_salary_user.salary < user.salary:
                max_salary_user = user

        for user in self.__users:
            if max_salary_user.salary == user.salary:
               user_list.append(user)

        return user_list

    def get_user_with_max_total(self):
        max_total_user = self.__users[0]
        for user in self.__users:
            if max_total_user.salary < user.total:
                max_total_user = user
        return max_total_user

    def get_user_by_name(self, name):
        for user in self.__users:
            if user.name == name:
                return user
        return None

    def __str__(self):
        return str(self.__users)
