h=5
for i in range(h):
    print(" "*(h-i), "*"*(i*2+1))
for i in range(h-2, -1, -1):
    print(" "*(h-i), "*"*(i*2+1))
