class Animal:
    def __init__(self, name, species):
        self.name = name  # 動物名稱
        self.species = species  # 物種類別
        self.__age = 18  # 私有屬性

    def speak(self):
        print(f"{self.name}動物發出聲音")

    def __private_fun(self):  # 私有方法
        print("I am private fun")


if __name__ == '__main__':
    # 創建對象
    my_animal = Animal("MyDog", "汪汪")
    print(f"My name is {my_animal.name}")   # 訪問對象的屬性
    my_animal.speak()  # 訪問對象的方法
    # print(my_animal.__age)  # 直接訪問私有屬性，不合法
    # my_animal.__private_fun()  # 直接訪問私有方法，不合法
