''' find the longest alphabetical order string '''

def str_add(a,s):
    global flag
    if ord(a[-1]) <= ord(s):
        a = a + s
    else:
        flag = False
    return a

s = 'abcdfkdslfjasabcfkdlsaefg'
s = 'abcabcd'
s = 'fksdlfjsdlfjlsdafs'
s = 'azcbobobegghakl'
s = 'abcbcd'
string_array = ['']


# TODO: CORRECT THESE
s = 'zyxwvutsrqponmlkjihgfedcba'
# s = 'utzslpatah'
# s = 'txemwtgytfwquhiqimmlng's

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

longest = ''
longest_len = 0

for i in range(1,len(string_array)):
    if len(string_array[i-1]) < len(string_array[i]):
        longest = string_array[i]
    elif len(string_array[i-1]) == len(string_array[i]):
        continue


print('Longest substring in alphabetical order is:', longest)
print(string_array)
