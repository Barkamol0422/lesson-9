a=int(input())
b=int(input())
c=int(input())
d=(a+b+c)/3
if d>a and d>b and d>c:
    print('All of these numbers are lesser than average')
elif d>a and d>b:
    print('only',a,' and ',b,'lesser than average')
elif d>b and d>c:
    print('only',b,' and ',c,'lesser than average')
elif d>a and d>c:
    print('only',a,' and ',c,'lesser than average')
elif d>a:
    print('only ',a,'is lesser than average')
else:
    print('Invalid input')
    
