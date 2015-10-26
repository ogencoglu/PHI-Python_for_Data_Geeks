# Basics - part 2

c = range(10)
print(c)
    
h = [i**i for i in c]
print(h)

# zip
def diff(x , y):
    return x-y
    
a = range(10)
b = a[::-1]
for a_el, b_el in zip(a,b):
    print(diff(b_el, a_el))
    
# Functional programming : lambda
# example 1
f = lambda x: x**2 + 2*x
f(5)

# example 2
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(mult3)
