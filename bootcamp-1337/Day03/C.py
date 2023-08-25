mod = 1000000007
def fact(nbr):
    if nbr == 0 or nbr == 1:
        return 1
    return (nbr * fact(nbr - 1)) % mod

def Pow(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        y = Pow(a, b // 2)
        return ((y * y) % mod)
    else:
        return ((a * Pow(a, b - 1)) % mod)

str_input = input()
dict = {}
for i in str_input:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    
result = fact(len(str_input))
for count in dict.values():
    result = (result * Pow(fact(count), mod - 2)) % mod  
print(result)

