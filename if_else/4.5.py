"""Даны координаты точки, не лежащей на координатных осях OX и OY. 
Определить номер координатной четверти, в которой находится данная точка. 
Координаты задаются пользователем, например (10, 15)."""

x, y = int(input("Enter coordinat x: ")), int(input("Enter coordinate y: "))

if x > 0 and y > 0:
    print("The point is in the 1st quadrant")
elif x < 0 and y > 0:
    print("The point is in the 2nd quadrant")
elif x < 0 and y < 0:
    print("The point is in the 3rd quadrant")
else:
    print("The pont is in the 4th quadrand")



