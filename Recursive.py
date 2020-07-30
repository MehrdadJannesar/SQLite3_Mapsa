# 1 + 2 + 3 + 4 + 5 == 15
# c + R(c-1)
#counter
# def counter(c):
#     if c <= 0 :
#         return c
#     else:
#         return c + counter(c-1)
#
#
# print(counter(5))
#fac
# 1 * 2 * 3 * 4 * 5 == 120
# n * R!(n-1)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
