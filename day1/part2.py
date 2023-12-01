import string

with open("example2.txt", "r") as f:
    st = f.readlines()

replaces = {'one':'1', 'two':'2', 'three':'3', 
            'four':'4', 'five':'5', 'six':'6', 
            'seven':'7', 'eight':'8', 'nine':'9'}

res = 0

for sub in st:
    tmp = ''.join(x for x in sub)
    print(replaces.keys())
    print(tmp)
print(res)


