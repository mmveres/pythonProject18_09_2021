from lesson05.users import *

def main():
    users = get_users_from_file("user1.txt")
    print(users)
    #  users[2][3] = "Vasya"
    cities = get_cities_from_users(users)
    print(cities)
    cities_list = list(cities)
    print(cities_list)
    ages = get_ages_from_users(users)
    print(ages)
    # ages[1]="Vasya"
    print(ages)
    print(max(ages))
    name_users = get_name_users_from_cities(users, "Poltava")
    print(name_users)

def convert_list_to_str(elems, delimetr=" "):
    str_elems = ""
    for el in elems:
        str_elems+=str(el) + delimetr
    return str_elems



def write_to_file_txt(filename, delimetr=" "):
    with open(filename, "w") as file_dig:
        for el in elems:
            file_dig.write(convert_list_to_str(el,delimetr) + "\n")

def write_to_file_csv(filename):
    with open(filename, "w") as file_dig:
        for el in elems:
            file_dig.write(convert_list_to_str(el,delimetr=";") + "\n")


if __name__ == '__main__':
    #main()
    elems = [(1, "Name1", "Age1", "City1"),(2, "Name2", "Age2", "City2")]
    #write_to_file_txt("user2.txt")
    #write_to_file_csv("user2.csv")
    users_list = get_users_from_file("user2.csv", ";")
    print(users_list)