#WAP to check the occurrence of vowels in a string

#{a,e,i,o,u}
'''
letter = input("Enter a letter: ")
letter= letter.lower()
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for char in letter:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1
print("Occurrences of vowels:")
print("A:", count_a)
print("E:", count_e)
print("I:", count_i)
print("O:", count_o)
print("U:", count_u)
'''


word=input("Enter a number: ")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,"occured",v,"times")