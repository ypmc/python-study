from user_test import user


# method using decorator
def get_singleton(cls):
    def get_instance(*args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = cls(*args, **kwargs)
        return cls.instance

    return get_instance


@get_singleton
class SingletonWithDecorator:
    def __init__(self, name, password):
        self._name = name
        self._password = password

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def __repr__(self):
        return 'name is {0}, password is {1}'.format(self._name, self._password)


# method 2 using '__new__' __new__ is the method called before __init__, it's the method that creates the object and
# returns it while __init__ just initializes the object passed as parameter you rarely use __new__, except when you
# want to control how the object is created.
class SingletonWithNew:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, password):
        self._name = name
        self._password = password

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def __repr__(self):
        return 'name is {0}, password is {1}'.format(self._name, self._password)


# method 3
# using metaclass
class UserMetaclass(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SingletonWithMetaclass(metaclass=UserMetaclass):
    def __init__(self, name, password):
        self._name = name
        self._password = password

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    def __repr__(self):
        return 'name is {0}, password is {1}'.format(self._name, self._password)


if __name__ == '__main__':
    name0 = 'test0'
    name1 = 'test1'
    password0 = 'password0'
    password1 = 'password1'

    print('singleton using decorator')
    user0 = SingletonWithDecorator(name0, password0)
    user1 = SingletonWithDecorator(name1, password1)
    print("user0 == user1 is {0}".format(user0 == user1))
    print("user0 is {0}".format(user0))
    print("user1 is {0}".format(user1))
    print('########################################################################################')
    print('singleton using __new__ method')
    singleton0 = SingletonWithNew(name0, password0)
    singleton1 = SingletonWithNew(name1, password1)
    print("singleton0 == singleton1 is {0}".format(singleton0 == singleton1))
    print("singleton0 is {0}".format(singleton0))
    print("singleton1 is {0}".format(singleton1))
    print('########################################################################################')
    print('singleton using meta class')
    metaUser0 = SingletonWithMetaclass(name0, password0)
    metaUser1 = SingletonWithMetaclass(name1, password1)
    print("metaUser0 == metaUser1 is {0}".format(metaUser0 == metaUser1))
    print("metaUser0 is {0}".format(metaUser0))
    print("metaUser1 is {0}".format(metaUser1))

    print('########################################################################################')
    print('singleton using import')
    importUser0 = user
    importUser1 = user
    importUser0.set_name(name1)
    print("importUser0 == importUser1 is {0}".format(importUser0 == importUser1))
    print("importUser0 is {0}".format(importUser0))
    print("importUser1 is {0}".format(importUser1))
