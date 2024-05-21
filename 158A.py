a,b = input().split(' ')
l = input().split(' ')
# a,b = 4,'2'
# l =[0,0,0,0]
k = l[int(b)-1]
qualified = [ int(score)  for score  in l if int(score) >= int(k) and int(score) > 0 ]
print(len(qualified))
