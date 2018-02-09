# 删除列表中的重复元素，并且保持原有顺序
from collections import Counter
from itertools import groupby
from operator import itemgetter, attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    print(sorted(users, key=attrgetter('user_id')))


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_non_hash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# zip 创建的是只能访问一次的迭代器
# 字典上的运算仅仅作用于键，而不是值
if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(zip(prices.values(), prices.keys())))
    print(max(zip(prices.values(), prices.keys())))
    print(prices_and_names)
    print(min(prices_and_names))  # OK
    # print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())

    # 删除列表中的重复元素，并且保留原有顺序
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe_non_hash(a, key=lambda d: (d['x'], d['y']))))

    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 8, 3)
    print(a.start)
    print(a.stop)
    print(a.step)
    s = 'HelloWorld'
    a.indices(len(s))
    for i in range(*a.indices(len(s))):
        print(s[i])

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_counts = Counter(words)
    print(word_counts.most_common(3))
    word_counts.update()

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    # 使用lambda表达式
    print(sorted(rows, key=lambda item: item['fname']))
    print(sorted(rows, key=lambda item: item['uid']))
    print(sorted(rows, key=lambda item: (item['uid'], item['fname'])))
    # 使用itemgetter速度更快
    print(sorted(rows, key=itemgetter('fname')))
    print(sorted(rows, key=itemgetter('uid')))
    print(sorted(rows, key=itemgetter('uid', 'fname')))
    # User sorted
    sort_notcompare()

    # group by
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)
