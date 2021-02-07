x, y = (map(int, input().split()))

def GCD(a, b):
     #a:큰값, b:작은값
    rest = 1
    while rest != 0:
        rest = a % b
        a = b
        b = rest
    return a
     
gcd = GCD(max(x,y), min(x,y))
print(x+y-gcd)

