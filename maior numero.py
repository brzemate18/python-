a=int(input('digite um numero de a '))
b=int(input('digite um numero de b'))
c=int(input('digite um numero de c'))
if a>b and a>c:
    print('a maior numero e',a)
elif b>a and b>c:
    print('a maior numero e',b)
elif c>b and c>a:
    print('a maior numero e',c)
elif a==b and a>c:
    print('empate e ' , a, b )
elif b==c and b>c:
    print('empate e', a,  c)
elif c==a and a>b:
    print('empate e', b , c)
else:
    print("empate de dois ou mais numeros ")


