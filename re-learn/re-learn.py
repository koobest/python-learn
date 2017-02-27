#re-learn.py
# to learn more about re module ,goto link: https://docs.python.org/2/library/re.html?winzoom=1

import fileinput,re

file_pat=re.compile(r'\[(.+?)\]') #非贪婪匹配，eg [hi word] [hello word] 将只匹配到[hi word] ，
            #这里是函数                      #贪婪匹配时,会匹配[hi word] [hello word]
                                 
scope={}

def replacement(match):
    code = match.group(1)
    try:
        tt = code
        return eval(code,scope) #通过键值取对应元素的值
    except SyntaxError:
        exec(code,scope) #eg:code = "name = 'lisi'",scope = {}  exec(code,scope)
                         #scope字典中会添加'name':'lisi' 键值对
        return ''

lines=[]

for line in fileinput.input():
    lines.append(line)
text = ''.join(lines) #拼接链表中的字符串
print(text)
print("*********************************")
#print(file_pat.sub(replacement,text).strip()) #先进行替换，替换完成就返回被替换的内容(，不是text的内容，text的内容不会被修改，而是返回另一字符串)
                                      #这里是方法，会将完整的内容替换掉，包括'[ ]'，因为匹配的就是'[.+?]'
st = file_pat.sub(replacement,text).strip()
print(st)
