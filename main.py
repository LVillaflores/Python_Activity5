def areacalculator():
    _input_ = input("Enter the shape you want to calculate area of: ")
    area = 0
    pie = 3.14
    cap = _input_.capitalize()
    if cap == "1":
        side = int(input("Enter the value of side: "))
        area = area + (side ** 2)
    elif cap == "4":
        radius = int(input("Enter the value of radius: "))
        area = area + (2 * pie * radius)
    elif cap == "2":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of length: "))
        area = area + (length * width)
    elif cap == "3":
        base = int(input("Enter the value of base: "))
        height = int(input("Enter the value of height: "))
        area = area +(0.5 * base * height)
    elif cap == "5":
        base1 = int(input("Enter the value of base 1: "))
        base2 = int(input("Enter the value of base 2: "))
        height = int(input("Enter the value of height: "))
        area = area + ((base1+base2/2)*height)
    else:
        print ("Select a valid shape")
    print ("%.2f" % area)
print("Menu")
print("1 - Square")
print("2 - Rectangle")
print("3 - Triangle")
print("4 - Circle")
print("5 - Trapezoid")
areacalculator()