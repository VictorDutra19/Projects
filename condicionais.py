"""
if,else e elif
"""
import random
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
d = random.randint(1,10)
e = random.randint(1,10)
print(f' {a}+{b}')

num1 = int(input())
if a+b == num1:
    ac1=1
    print(f'acertou!')
else:
    ac1=0
    print(f'a resposta certa é {a+b}')
print(f' {c}+{b}')

num2 = int(input())
if c+b == num2:
    ac2=1
    print(f'acertou!')
else:
    ac2 = 0
    print(f'a resposta certa é {c+b}')
print(f' {d}+{e}')

num3 = int(input())
if e+d == num3:
    ac3 = 1
    print(f'acertou!')
else:
    ac3 = 0
    print(f'a resposta certa é{d+e}')
print(f' {c}+{e}')

num4 = int(input())
if c+e == num4:
    ac4=1
    print(f'acertou!')
else:
    ac4=0
    print(f'a resposta certa é{c+e}')

print(f' {a}+{d}')

num5 = int(input())
if a+d == num5:
    ac5=1
    print(f'acertou!')
else:
    ac5=0
    print(f'a resposta certa é{a+d}')
print(f'Questões acertadas foram {ac1+ac2+ac3+ac4+ac5}')






