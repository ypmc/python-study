class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __eq__(self, other):
        print("id is {0}, name is {1}".format(other.get_id(), other.get_name()))
        return self.get_id() == other.get_id()

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    # 将方法变为属性
    @property
    def get_address(self):
        return 'SH'

    def __pos__(self):
        print('__pos__')
        return 'positive user'

    def __neg__(self):
        print('__neg__')
        return 'negative user'


if __name__ == '__main__':
    u1 = User(1, 'admin')
    u2 = User(1, 'test')
    print(u1 == u2)
    print(u1.__dict__)
    print(u1.get_address)
    print(+u1)
    print(-u1)
    x = 1
    x += 1
    print(x)
