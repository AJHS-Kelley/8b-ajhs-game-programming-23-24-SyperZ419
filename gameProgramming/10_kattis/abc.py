numbers = input()
a, b, c = numbers.split()
a = int(a)
b = int(b)
c = int(c)

#print(f"a: {a}, b: {b}, c: {c}")
if a >= b:
    a, b = b, a

if b >= c:
    b, c = c, b
if b <= a:
    a, b = b, a
#print(f"a: {a}, b: {b}, c: {c}")

# input string variable
# determine order of A, B, C
# create correct string
# output string

order = input()
string = ""

for i in range(len(order)):
    if order[i] == "A":
        string += str(a) + " "
    elif order[i] == "B":
        string += str(b) + " "
    else:
        string += str(c) + " "

print(string)