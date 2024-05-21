n = int(input(""))
counts = 0 
for i in range(n):
    i = input("").split(" ")
    i = [ int(x) for x in i ]
    if sum(i) >= 2 :
        counts+=1
        
print(counts)
