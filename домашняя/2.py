#Даны три целых числа. Выведите значение наименьшего из них.
x=int(input("введите x"))
y=int(input("введите y"))
z=int(input("введите z"))
if x<y and x<z:
    print(x)
elif y<x and y<z:
    print(y)
else: print(z)