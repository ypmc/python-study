import json

some_list = [1, 2, 3, 4, 5, 2, 5, 1, 4, 8]
even_set = [x for x in some_list if x % 2 == 0]
print(type(even_set))
print(type(set(even_set)))
print(set(even_set))

data = {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": True},
                                                {"age": 29, "name": "Joe", "lactose_intolerant": False}]}
print(json.dumps(data, indent=2))

print("Hello %(name)s !" % {'name': 'James'})
print("I am years %(age)i years old" % {'age': 18})
print("Hello {name} !".format(name="James"))

a = [1, 2, 3, 4, 5]
print(a[::3])
Name = "Hello" "World"
print(Name)
range(4)
for _ in range(5):
    print(_)

L = [(i, j) for i in range(3) for j in range(i)]
print(L)
L = [i for i in range(3)]
print(L)

try:
    print(1)
    print('test')
except Exception as e:
    print(e)
else:
    print('ok')
finally:
    print('finally')

print(pow(2, 4, 3))
lst = ["a", "b", "c"]
print(list(enumerate(lst)))
