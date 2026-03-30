idade=int(input("Qual a sua idade?"))
if idade>=18:
    print("Adulto")
elif idade>=13:
    print("Adolescente")
elif idade>=2:
    print("Criança")
elif idade<=-1:
    print("Negado")
else:
    print("Bebê")
