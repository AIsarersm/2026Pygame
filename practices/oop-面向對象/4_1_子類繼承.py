
class Animal:
    def __init__(self, name, species):
        self.name = name  # 動物名稱
        self.species = species  # 物種類別
        self.__age = 18  # 私有屬性

    def speak(self):
        print(f"{self.name}動物發出聲音")

    def __private_fun(self):  # 私有方法
        print("I am private fun")

    def is_adult(self):   # 通過創建一個public的方法，向外透露自身的private成員的相關
        if self.__age >= 18:
            return "我成年了"
        else:
            return "我未成年"


class Dog(Animal):  # 子類，繼承Animal類
    def __init__(self, name, species, color):
        super().__init__(name, species)  # 父類進行初始化
        self.color = color

    def bark(self):
        print(f"I am {self.color} {self.name}, my species is {self.species}")  # 使用父類和自身的尉性

    # def try2GetFatherPrivate(self):  # wrong, cannot visit father private member and function
    #     print(f"{self.__private_member}")
    #     print(f"{self.__private_function()}")


if __name__ == '__main__':
    # 創建對象
    my_animal = Animal("Name_a", "汪汪")
    print(f"My name is {my_animal.name}")   # 訪問對象的屬性
    my_animal.speak()  # 訪問對象的方法
    print("*********************************")

    # 創建子類對象
    my_dog = Dog("Name_b", "Golden Hair", "Gold")
    print(f"My name is {my_dog.name}")  # 訪問對象父類的屬性
    print(f"My color is {my_dog.color}")  # 訪問對象自身的屬性
    my_dog.speak()  # 使用父類方法
    my_dog.bark()  # 使用自身方法
    # my_dog.try2GetPrivate()  #不合法
