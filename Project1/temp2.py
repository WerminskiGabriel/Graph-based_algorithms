def is_prime( x ) :
    if x <= 1 :
        return False

    if x == 2 or x == 3 or x == 5 :
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 :
        return False
    i = 5
    while i * i <= x :
        if x % i == 0 or x % (i+2) == 0 :
            return False
        i += 6
    return True

res = "["
cnt = 0
i = 0
while cnt != 1000 :
    if is_prime( i ) :
        cnt += 1
        res += f"{i},"
    i += 1
res = res[:-1]
res += "]"
print( res )