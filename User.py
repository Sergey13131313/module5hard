class User:
    """Класс пользователя UrTube"""

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return [self.nickname, self.password] == other

    def showUser(self):
        print('{:<25}{:>25}'.format('Имя пользователя - ', self.nickname))
        print('{:<25}{:>25}'.format('Пароль - ', self.password))
        print('{:<25}{:>25}'.format('Возраст пользователя - ', self.age))


if __name__ == '__main__':
    user1 = User('Aaa', '111', 20)
    user2 = User('Aaa', '111', 20)

    print(user1 == ['Aaa', hash('111')])
