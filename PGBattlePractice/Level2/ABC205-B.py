# from 11:02 end 23:07
# sorted(LIST) はもとのリストを変更しない
# LIST.sort()はLISTをソートする、sort()自体はNoneをかえすので注意
n = int(input())
A = list(map(int, input().split()))
if sorted(A) == [i for i in range(1,n+1)]:
    print("Yes")
else:
    print("No")