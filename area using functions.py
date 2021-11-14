def area_square():
    side =  eval(input("Input the length of square: "))
    print("The area of the square is:", side*side)
def area_circle():
    rad = eval(input("Input the radius of the circle: "))
    print("The area of the circle is: ",3.14*rad*rad)
def area_rectraingle():
    length,breadth=eval(input("Enter the length and breadth of rectraingle: "))
    print("The area of the rectraingle is: ",length*breadth)
def area_triangle():
    a,b,c=eval(input("Enter the 3 sides of a triangle: "))
    s=(a+b+c)/2
    print("The area of the triangle is: ",(((s-a)+(s-b)+(s-c))**0.5))
choice=int(input("Choice: 1-square, 2-circle, 3-rectangle, 4-triangle:"))
if choice ==1:
    area_square()
elif choice == 2:
    area_circle()
elif choice ==3:
    area_rectraingle()
elif choice ==4:
    area_triangle()
else:
    print("Not a valid choice")