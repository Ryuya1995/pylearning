import turtle

tr = turtle.getturtle()

def koch(n,len):
    if(n==0):
        tr.forward(len)
    elif(n==1):
     tr.forward(len/3.0)
     tr.left(60)
     tr.forward(len/3.0)
     tr.right(120)
     tr.forward(len/3.0)
     tr.left(60)
     tr.forward(len/3.0)
    else:
        koch(n-1,len/3.0)
        tr.left(60)
        koch(n-1,len/3.0)
        tr.right(120)
        koch(n-1,len/3.0)
        tr.left(60)
        koch(n-1,len/3.0)

if __name__ == '__main__':
    koch(2, 300)