# find the longest common sufix substring from any list of string.

ls = ["monday","monday","monday"]
ls.sort()
print(ls)
ln = min(len(ls[0]),len(ls[-1]))
print(ln)
blanck = ""
for i in range(1,ln+1):
    if (ls[0][-i] == ls[-1][-i]):
        blanck=ls[0][-i]+blanck
    else:
        break
print(blanck)
        