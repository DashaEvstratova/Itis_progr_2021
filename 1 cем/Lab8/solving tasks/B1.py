def move(n,x,y):
    if n > 0:
        move(n-1,x,y)
        print(n,x,2)
        move(n-1,y,x)
        print(n,2,y)
        move(n-1,x,y)
    return n,x,y
   
move(2,1,3)