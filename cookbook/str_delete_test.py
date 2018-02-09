s = ' hello world \n'
print(len(s))
a = s.strip()
print(len(a))
print(a)
print('lstrip', s.lstrip())
print('rstrip', s.rstrip())
print('end')
g = '''hello
    icbc
'''
print(g.strip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
