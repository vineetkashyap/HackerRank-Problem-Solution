if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
res=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            res.append([i,j,k])
my_list = list(p for p in res if p[0]+p[1]+p[2] != n)
print(my_list)
