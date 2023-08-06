r = float(input(' Please Enter the radius of a circle: '))
PI = 3.14

area = PI * r * r

print(" Area Of a Circle = %.2f" %area)

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
def area_of_trianle(first_side,second_side,third_side):
    s = (first_side + second_side + third_side) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# calculate the area

print('The area of the triangle is ', area_of_trianle(a,b,c))