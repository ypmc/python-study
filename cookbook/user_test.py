class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password

    def __repr__(self):
        return 'user in user_test, name is {0}, password is {1}'.format(self._name, self._password)

    def set_name(self, value):
        self._name = value

    def set_password(self, value):
        self._password = value


user = User('name', 'password')
