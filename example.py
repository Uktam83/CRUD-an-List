'''
1 2 3
4 5 6
7 8 9
'''
s=0
a=[]
n = int(input())
for i in range(n):
    ans=[int(i) for i in input().split()]
    if len(ans)!=n:
        break
    else:

        ss=sum(ans)
        #a.append(ss)
        s+=ss
print(f"summa = {s}")
'''
test 1
4
1 2 3 4
5 4 3 2
6 5 4 3
7 6 5 4
....

'''