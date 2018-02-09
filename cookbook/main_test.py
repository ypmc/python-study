from variable_test import *


def fibonacci(n):
    a, b = 1, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n = n - 1


if __name__ == '__main__':
    a = Article(2, 'test')
    print(a.__dict__)
    print(a._id)
    print(a._title)
    print(a._Article__private_in_class)
    print(COMMON_VAR)
    # print(_private_in_module)
    g = fibonacci(10)
    for a in g:
        print(a)

    print(hash('hello world'))
    print(hash('123'))
    print(hash(234))

    print('a is %s' % a)
