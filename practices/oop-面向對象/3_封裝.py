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


if __name__ == '__main__':
    # 創建對象
    my_animal = Animal("MyDog", "汪汪")
    print(f"My name is {my_animal.name}")   # 訪問對象的屬性
    my_animal.speak()  # 訪問對象的方法
    print(my_animal.is_adult())  # 通過接口訪問到類的私有屬性相關

