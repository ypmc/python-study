import re
from calendar import month_abbr

line = 'asdf fjdk; afed, fjek,asdf, foo'
lst = re.split(r'[;,\s]\s*', line)
print(type(lst))
print(lst)
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# 确保非捕获数组, 格式 ?:, 与中括号一致
lst = re.split(r'(?:,|;|\s)\s*', line)
print(lst)

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
lst = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)
print(lst)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
lst = datepat.sub(r'\3-\1-\2', text)
print(lst)


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    print('month name is ', mon_name)
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.sub(change_date, text)
lst = datepat.sub(change_date, text)
print(lst)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
newtext, n = datepat.subn(r'\3-\1-\2', text)
print('newtext is ', newtext, ' replace number is ', n)

text = 'UPPER PYTHON, lower python, Mixed Python'
lst = re.findall('python', text, flags=re.IGNORECASE)
print(lst)
text = 'UPPER PYTHON, lower python, Mixed Python'
lst = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(lst)


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


text = 'UPPER PYTHON, lower pyTHon, Mixed Python'
lst = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(lst)

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
lst = str_pat.findall(text1)
print(text1)
print(lst)
text2 = 'Computer says "no." Phone says "yes."'
lst = str_pat.findall(text2)
print(text2)
print(lst)

text2 = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'\"(.*?)\"')
lst = str_pat.findall(text2)
print(text2)
print(lst)

comment0 = re.compile(r'/\*(.*?)\*/')
comment1 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multi-line comment */
 '''
lst = comment0.findall(text1)
print(lst)
lst = comment0.findall(text2)
print(lst)
lst = comment1.findall(text2)
print(lst)
lst = comment2.findall(text2)
print(lst)

num = re.compile('\d+')
lst = num.match('123')
print(lst)
print(lst.group())
lst = num.match('\u0661\u0662\u0663')
print(lst)
