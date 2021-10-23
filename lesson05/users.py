def get_cities_from_users(users):
    cities = []
    for user in users:
        cities.append(user[3])
    return tuple(cities)

def get_name_users_from_cities(users,city):
    names = []
    for user in users:
        if (user[3] == city):
            names.append(user[1])
    return tuple(names)

def get_ages_from_users(users):
    ages_list = []
    for user in users:
        ages_list.append(int(user[2]))
    return tuple(ages_list)


def get_users_from_file(filename="user.txt", delimetr=" "):
    users = []
    with open(filename, "r") as file_dig:
        for el in file_dig:
            #  el1 = el.replace("\n","")
            #  elems = el1.split(" ")
            elems = el.strip().split(delimetr)
            users.append(tuple(elems))
    return users

if __name__ == '__main__':
    users = [(1,"Name1","Age1","City2"),(2,"Name2","Age2","City2")]
    names = get_name_users_from_cities(users, "City2")
    print(names)