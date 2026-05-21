class Animal:
    def __init__(self, name, species):
        self.name = name  # 動物名稱
        self.species = species  # 物種類別
        self.__age = 18  # 私有屬性

    def speak(self):
        print(f"{self.name}動物發出聲音")

    def __private_fun(self):  # 私有方法
        print("I am private fun")

    def is_adult(self):  # 通過創建一個public的方法，向外透露自身的private成員的相關
        if self.__age >= 18:
            return "我成年了"
        else:
            return "我未成年"

    def run(self):
        print("Slow run")


class Dog(Animal):  # 子類，繼承Animal類
    def __init__(self, name, species, color):
        super().__init__(name, species)  # 父類進行初始化
        self.color = color

    def bark(self):
        print(f"I am {self.color} {self.name}, my species is {self.species}")  # 使用父類和自身的尉性

    def run(self):  # 父類方法重寫
        print(f"{self.name}: Fast Run")


if __name__ == '__main__':
    # 創建Dog對象1
    my_dog_1 = Dog("Name_b", "Golden Hair", "Gold")
    my_dog_1.run()

    # 創建Dog對象2
    my_dog_2 = Dog("Name_c", "Corgi", "White")
    my_dog_2.run()
