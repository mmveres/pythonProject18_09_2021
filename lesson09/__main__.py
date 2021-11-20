import sqlite3
class Employee:
    def __init__(self, name , surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Empl: {self.name}, {self.surname}\n"

    def __repr__(self):
        return self.__str__()

class EmployeeDAO:
    def __init__(self):
        self.conn = sqlite3.connect("Chinook_Sqlite.sqlite")
        self.cursor = self.conn.cursor()

    def get_employee_list(self):
        self.cursor.execute("SELECT * FROM Employee")
        result_list = self.cursor.fetchall()
        emp_list = list()
        for res in result_list:
            emp_list.append(Employee(res[1], res[2]))
        return emp_list

    def get_employee_list_by_name(self, name):
        self.cursor.execute(f"SELECT * FROM Employee WHERE Employee.FirstName = '{name}'")
        result_list = self.cursor.fetchall()
        emp_list = list()
        for res in result_list:
            emp_list.append(Employee(res[1], res[2]))
        return emp_list

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    empl_dao = EmployeeDAO()
    emp_list = empl_dao.get_employee_list_by_name("Steve")

    print(emp_list)
    empl_dao.close()