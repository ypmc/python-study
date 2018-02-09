import html

s = 'Elements are written as "<tag>text</tag>".'
print(html.escape(s))
print(html.escape(s, quote=False))
