class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 2:
            self.__name = new_name
        else:
            raise ValueError("Ism eng kamida 3ta harfdan iborat bolishi kerak")
    @age.setter
    def age(self, new_age):
        if (new_age) >= 1:
            self.__age = new_age
        else:
            raise ValueError("Yosh eng kamida 1 yoki undan katta bolishi kerak")
        
user = User(name="Abdullaxoja", age=2)
print(user.name)
print(user.age)

user.name = "Men"
print(user.name)

user.age = 10
print(user.age)