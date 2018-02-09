import sys

import unicodedata

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)
b = unicodedata.normalize('NFD', a)
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(b.translate(cmb_chrs))

a = 'test'
b = 'icbc'
print('{} {}'.format(a, b))


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


g = sample()
print(type(g))
for s in g:
    print(s)

print(''.join(sample()))

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))
name = 'Guido'
n = 49
print(vars())
print(s.format_map(vars()))


class safesub(dict):
    """防止key找不到"""

    def __missing__(self, key):
        return '{' + key + '}'


del n  # Make sure n is undefined
print(s.format_map(safesub(vars())))


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))