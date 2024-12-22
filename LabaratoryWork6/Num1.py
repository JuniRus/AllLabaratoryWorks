class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, password):
        self.__password = password
    def check_password(self, password):
        return  self.__password == password
    def show_password(self):
        print(self.__password)

obj = UserAccount("Павел", "pavel2006@email.com", "cookies")
print("Пароль до изменения: ", end='')
obj.show_password()

obj.set_password("pasha_sigma2006")

print("Пароль после изменения: ", end='')
obj.show_password()
print(f"Проверить совпадение пароля: {obj.check_password("cookies")}")