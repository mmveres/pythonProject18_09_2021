from lesson07.kmda.user import User

def get_users_from_file(self, filename):
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

def save_users_to_json(self, filename, users):
    #TODO: implement
    pass

def load_users_from_json(self, filename):
    #TODO: implement
    pass
