class Animal:
    def __init__(self, name, species):
        self.name = name  # 動物名稱
        self.species = species  # 物種類別

    def speak(self):
        print(f"{self.name}動物發出聲音")


if __name__ == '__main__':
    # 創建對象
    my_animal = Animal("MyDog", "汪汪")
    print(f"My name is {my_animal.name}")   # 訪問對象的屬性
    my_animal.speak()  # 訪問對象的方法
