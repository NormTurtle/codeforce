n = int(input(""))
count = 0
for i in range(n):
    i = input('')
    if '--' in i:
        count-=1
    if '++' in i:
        count+=1
print(count)
