class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name, self.surname
        return full_name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


work_info = Position('Ivan', 'Ivanov', 'seller', 10000, 1000)
print(work_info.get_full_name())
print(work_info.get_total_income())









