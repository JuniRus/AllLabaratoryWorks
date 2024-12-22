class Employee:
    def __init__(self, name, id, **kwargs):
        self._name = name
        self.id = id
        super().__init__(**kwargs)
    def get_info(self):
        print(f"Имя сотрудника: {self._name}; "
              f"Идентификационный номер: {self.id}")

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)
    def manage_project(self):
        pass
    def get_info(self):
        print(f"Имя сотрудника: {self._name}; "
              f"Идентификационный номер: {self.id}; "
              f"Отдел: {self.department}")

class Technician(Employee):
    def __init__(self, specialization, **kwargs):
        self.specialization = specialization
        super().__init__(**kwargs)
    def perform_maintenance(self):
        pass
    def get_info(self):
        print(f"Имя сотрудника: {self._name}; "
              f"Идентификационный номер: {self.id}; "
              f"Специализация: {self.specialization}")

class TechManager(Manager, Technician):
    employees = []

    def __init__(self, name, id, department, specialization):
        super().__init__(name = name, id = id, department = department, specialization = specialization)
    def add_employee(self, employee):
        self.employees.append(employee)
    def get_team_info(self):
        for employee in self.employees:
            employee.get_info()
    def get_info(self):
        print(f"Имя сотрудника: {self._name}; "
              f"Идентификационный номер: {self.id}; "
              f"Отдел: {self.department}; "
              f"Специализация: {self.specialization}")


obj = TechManager("Антон",42,"Маркеттинг","Product Manager")

obj.add_employee(Employee(name = "Григорий", id = 1))
obj.add_employee(Technician(name = "Альберт", id = 2, specialization = "ремонт оборудования"))
obj.add_employee(Manager(name = "Стефан", id = 3, department = "разработка"))

obj.get_team_info()
obj.get_info()