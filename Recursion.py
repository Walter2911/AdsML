def factorial(n):
    if n == 0:
        return 1
    else:                                           # 221910312015(K.L.S.Akash)
        return n * factorial(n - 1)


print(factorial(int(input("Enter the desired num: "))))