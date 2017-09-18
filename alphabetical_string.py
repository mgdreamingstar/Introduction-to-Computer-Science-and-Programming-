''' find the longest alphabetical order string '''

def str_add(a,s):
    global flag
    if ord(a[-1]) < ord(s):
        a = a + s
    else:
        flag = False
    return a

s = 'abcdfkdslfjasabcfkdlsaefg'
s = 'abcabcd'
s = 'fksdlfjsdlfjlsdafs'
string_array = ['']

for i in range(len(s)):
    string = s[i]
    flag = True
    while flag:
        try:
            string = str_add(string,s[i+len(string)])
        except:
            break
    if len(string_array[-1]) <= len(string) :
        string_array.append(string)


print(string_array[-1])
