
def travel(x,y):
    n=s=w=e=0
    if x==1:
        if y==1:
            place = '(N)orth'
            n=1
        elif y==2:
            place = '(N)orth or (E)ast or (S)outh'
            n=e=s=1
        elif: y == 3:
            place = '(E)ast or (S)outh'
            e=s=1
    if x == 2:
         if y==1:
            place = '(N)orth'
            n=1
        elif y==2:
            place = '(W)est or (S)outh'
            w=s=1
        elif: y == 3:
            place = '(E)ast or (W)est'
            e=w=1
    if x == 3:
         if y==1:
            V = 1
        elif y==2:
            place = '(N)orth or (S)outh'
            n=s=1
        elif: y == 3:
            place = '(W)est or (S)outh'
            w=s=1

def direction(x,y,k):
    if k == 'N' or k == 'n':
        if n==0:
            ans="Not a valid direction!"
            return ans
        else:
            return x , y +1

    elif k == 'E' or k == 'e':
        if e==0:
            ans="Not a valid direction!"
            return ans
        else:
            return x+1 , y

    elif k == 'S' or k== 's':
        if s==0:
            ans="Not a valid direction!"
            return ans
        else:
            return x , y-1
    
    elif k == 'W' or k == 'w':
        if w==0:
            ans="Not a valid direction!"
            return ans
        else:
            return x-1 , y


x = 1
y = 1

while V!= 1:
    travel(x,y)
    k = input('Direction: ')

    







