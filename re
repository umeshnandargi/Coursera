import re

data = '''Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative
7 and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that
everyone needs to know how to program ...'''

nos = re.findall('[0-9]+', data)
for str in nos:
    nos[nos.index(str)] = int(str)
print(nos)


import re
line = '''
<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>
'''
print(re.findall('href="(.+)"' , line)) # gives Output: ['"http://www.dr-chuck.com/page2.htm"']


import re
txt = 'From stephen.marquarddd@uct.ac.za Sat Jan  5 09:14:16 2008'
print(re.findall('\S+@\S+' , txt ))
