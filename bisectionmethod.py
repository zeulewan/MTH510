low = -10
high = 10
c = None
def f(x):
    return (x*x*x - 2)
i = 0
while (f(low) * f(high) < 0):
    c = (low + high)/2

    if (abs(c - high) < 0.0001) or (abs(c - low) < 0.0001):
        print("root is x =", c)
        i = i + 1
        break
    else: 
        if(f(low) * f(c) < 0):
            i = i + 1
            high = c
        else: 
            if(f(high) * f(c) < 0):
                low = c
                i = i + 1

    print (c)
print(i)

if c is None:
    print("uneven # of roots in range")
