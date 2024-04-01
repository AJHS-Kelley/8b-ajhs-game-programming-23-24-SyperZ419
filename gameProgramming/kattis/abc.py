# input the integers
# .split() the 3 integers
# cast the 3 variables to integers
# assign correct values from least to greatest
# A < B < C

numbers = input()
a, b, c = numbers.split()
a = int(a)
b = int(b)
c = int(c)

print(f"a: {a}, b: {b}, c: {c}")
if a >= b:
    a, b = b, a

if b >= c:
    b, c = c, b
if b <= a:
    a, b = b, c
print(f"a: {a}, b: {b}, c: {c}")