
N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

x, y = 1,1
acceptable_moves = ('')
direction = ''


def travel(x, y, direction):
    

    if direction == 'n' or direction == 'N':
        return x, y + 1
    elif direction == 's' or direction == 'S':
        return x, y - 1
    elif direction == 'e' or direction == 'E':
        return x + 1, y
    elif direction == 'w' or direction == 'W':
        return x - 1, y

while True: 
    if direction in acceptable_moves:
        if ((x == 1) and (y == 1)) or ((x == 2) and (y == 1)):
            print("You can travel: {}.".format(N))
            acceptable_moves = ('n','N')   
        elif x == 1 and y == 2:
            print("You can travel: {} or {} or {}.".format(N,E,S))
            acceptable_moves = ('n', 'e', 's','N', 'E', 'S') 
        elif (x == 1) and (y == 3):
            print("You can travel: {} or {}.".format(E,S))
            acceptable_moves = ('e', 's', 'E', 'S') 
        elif ((x == 2) and (y == 2)) or ((x == 3) and (y == 3)):
            print("You can travel: {} or {}.".format(S,W))
            acceptable_moves = ('s', 'w', 'S','W') 
        elif (x == 2) and (y == 3):
            print("You can travel: {} or {}.".format(E,W))
            acceptable_moves = ('e', 'w','E','W') 
        elif (x == 3) and (y == 2):
            print("You can travel: {} or {}.".format(N,S))
            acceptable_moves = ('n', 's','N','S') 
        elif x == 3 and y == 1:
            print ('Victory!')
            break
      
    direction = input("Direction: ")
    if direction.lower() in acceptable_moves:
        x, y = travel(x, y, direction) # Sækja travel-functionið
    else:
        print ('Not a valid direction!')
        if ((x == 1) and (y == 1)) or ((x == 2) and (y == 1)):
            print("You can travel: {}.".format(N))
            acceptable_moves = ('n','N')   
        elif x == 1 and y == 2:
            print("You can travel: {} or {} or {}.".format(N,E,S))
            acceptable_moves = ('n', 'e', 's','N', 'E', 'S') 
        elif (x == 1) and (y == 3):
            print("You can travel: {} or {}.".format(E,S))
            acceptable_moves = ('e', 's', 'E', 'S') 
        elif ((x == 2) and (y == 2)) or ((x == 3) and (y == 3)):
            print("You can travel: {} or {}.".format(S,W))
            acceptable_moves = ('s', 'w', 'S','W') 
        elif (x == 2) and (y == 3):
            print("You can travel: {} or {}.".format(E,W))
            acceptable_moves = ('e', 'w','E','W') 
        elif (x == 3) and (y == 2):
            print("You can travel: {} or {}.".format(N,S))
            acceptable_moves = ('n', 's','N','S') 
        elif x == 3 and y == 1:
            print ('Victory!')
            break
        
        

    







