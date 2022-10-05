l, r = map(int, input().split())
s = input()
top = s[:l-1]
x = s[l-1:r]
middle = x[::-1]
tail = s[r:]
print("".join(top+middle+tail))
