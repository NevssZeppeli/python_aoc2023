import string

with open("input.txt", "r") as f:
    st = f.readlines()

res = 0
for sub in st:
    tmp = "".join(x for x in sub if x.isdecimal())
    if len(tmp) != 0: 
        res += int(tmp[0]+tmp[-1])
print(res)

