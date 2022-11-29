class Worker:
    def __init__(self, name, position, exp):
        self.name = name
        self.position = position
        self.exp = exp

    def print_info(self):
        print(self.name, self.position, self.exp)

    def empl(self, name, position, exp):
        self.worker  = Worker(name, position, exp)


empl1 = Worker('Иван', 'системный администратор', 3)
empl1.empl('Иван', 'системный администратор', 3)

a = empl1.worker.name
b = empl1.worker.position
c = empl1.worker.exp
print('Имя: ', a, 'Должность: ', b, 'Стаж: ', c)

