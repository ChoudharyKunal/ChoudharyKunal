a = "there are  2 apples for 4 person"

print(a)

res  = [int(i) for i in a.split() if i.isdigit()]
print(res)