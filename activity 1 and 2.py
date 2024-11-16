a=5
b=4
c=8
d=2
e=(a+b)*c/d
print(e)

a=input('Enter your name: ')
b=int(input('Enter your age: '))
if a.lower()=='alex' or a.lower()=='john' and b>=2:
    print('Welcome ', a)
else:
    print('Goodbye')
    exit()
