import inspect
import itertools
from variable_test import *

if __name__ == '__main__':
    horses = [1, 2, 3, 4]
    races = itertools.permutations(horses)
    print(type(races))
    print(list(races))

    a = Article(1, 'test')
    print('########################### using var ###########################')
    for prop, value in vars(a).items():
        print('%s = %s' % (prop, value))
    print('########################### using inspect ###########################')
    for attr, value in inspect.getmembers(a):
        print('%s = %s' % (attr, value))
    print('#####################################################################')
    print(a.__dict__)
    print(Article.__dict__)
    print(Article.get)
    print(a.get)

    lst = ["a", "b", "c"]
    print(list(enumerate(lst)))
    print(list(enumerate(lst, 5)))

    a, b = [], []
    a.append(b)
    b.append(a)
    print(a)
    print(len(a))