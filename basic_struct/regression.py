# x^m Θ(logn)
def power(x, m):
    if m == 0:
        return 1
    else:
        y = power(x, int(m/2))
        if m%2 == 0:
            return y*y
        else:
            return x*y*y


# x^m Θ(logn)
def exp(x, m):
    y = 1
    binary = []
    # 将10进制数n写成二进制形式
    while m!=0:
        binary.append(m%2)
        m = int(m/2)
    print(binary)
    for i in range(len(binary)-1, -1, -1):
        y = y*y
        if binary[i] == 1:
            y = x*y
    return y


print(exp(2, 10))