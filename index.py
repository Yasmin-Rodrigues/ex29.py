#Programa que leia 3 retas e verique se elas podem formar um triângulo 
a =float(input('Digite a primeira reta:'))
b =float(input('Digite a segunda reta:'))
c =float(input('Digite a terceira reta:'))
ra =b-c
rb =a-c
rc =a-b
print('Só formará um triângulo se TODOS os lados forem VERDADEIROS:')
if ra<a<b+c:
    print('Verdadeiro')
if rb<b<a+c:
    print('Verdadeiro')
if rc<c<a+b:
    print('Verdadeiro')
else:
    print('Falso')