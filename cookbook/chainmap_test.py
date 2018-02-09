from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
print(c['z'])  # Outputs 3 (from a)

print(type(c))
print(len(c))
print(list(c.keys()))
print(list(c.values()))
c['z'] = 10
c['w'] = 40
del c['x']
print(c)
print(a)
# 对于字典的更新或删除操作总是影响的是列表中第一个字典
# del c['y'] # output KeyError: "Key not found in the first mapping: 'y'"


values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print("values['x']", values['x'])
# Discard last mapping
values = values.parents
print("values['x']", values['x'])  # Discard last mapping
values = values.parents
print("values['x']", values['x'])
print(ChainMap({'x': 1}))

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
print('before update', merged)
merged.update(a)
print('after update ', merged)
a['x'] = 5
print(merged)
merged = ChainMap(a, b)
print(merged)
