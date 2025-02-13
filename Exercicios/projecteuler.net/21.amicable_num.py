import datetime
now = datetime.datetime.now()
def d(n):
    sum = 0
    for i in range(1, (n//2 + 1)):
        if n % i == 0:
            sum += i
    return sum


soma = 0
for a in range(2, 10001):
    b = d(a)
    if d(b) == a and a != b:
        soma += a  


print(soma)
after = datetime.datetime.now()
print(after - now)

 