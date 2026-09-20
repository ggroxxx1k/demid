import math 
a, b, c = [float(input(f'введите коэффициент {x}: ')) for x in ['a', 'b', 'c']]

if a == 0:
        print("коэффициент 'a' не может быть нулем")

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("два корня:", x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print("один корень:", x)
else:
    print("дискриминант меньше нуля, корней нет")
