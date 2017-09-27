
print("To calculate the area for each of the shapes, choose 1 for rectangle, 2 for circle and 3 for a triangle")
x = int(input())
if x==1:
    l , w = eval(input("Enter the length, width of the rectangle: "))
    rect = l*w
    print("The area of rectangle is", rect )

elif x==2:
    r = eval(input("Enter the radius of the circle" ))
    pi= 3.142
    cir = pi*r*r
    print("The area of the circle is", cir)

elif x==3:
    b , h = eval(input("Enter the base , height of the triangle :"))
    tri = 0.5*b*h
    print("The area of the triangle is", tri)
else :
    print("Try choosing a number between 1 and 3")















