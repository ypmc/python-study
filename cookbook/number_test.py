from decimal import Decimal, localcontext

import math

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(-1.23, 1))
print(round(1627731, -1))
print(round(1627736, -1))
print(round(1627731, -2))
print(round(1627731, -3))

a = Decimal('4.2')
b = Decimal('3.6')
print(a + b)
print(a + b == Decimal('7.8'))

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
print(math.fsum(nums))

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))