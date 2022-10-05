# from 22:43 end 22:56
# 一まとまりの数字は9行目のように取得するのがよい
def nex(n):
    if n == 9:
        return 0
    else:
        return n + 1

pas = [int(i) for i in list(input())]
if len(set(pas)) == 1:
    print("Weak")
elif nex(pas[0]) == pas[1] and nex(pas[1]) == pas[2] and nex(pas[2]) == pas[3]:
    print("Weak")
else:
    print("Strong")
