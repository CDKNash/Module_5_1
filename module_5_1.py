class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, new_floor + 1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")
                break
            print(i)


house1 = House('ЖК Изумрудный', 18)
house2 = House('Поселок ЦДК', 2)
house1.go_to(5)
house2.go_to(10)
