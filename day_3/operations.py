age = 16
height = 1.58
complex_number = 2+j
base = 20
height_triangle = 10
area_of_the_triangle = 100
base = input("¿cual es la base?")
print(f"la base es {base}")
height_triangle = input("¿cual es la altura")
print(f"la altura es {height_triangle}")
area_of_the_triangle = 0.5 * base * height_triangle
area_of_the_triangle = input("¿cual es el area?")
print(f"el area es {area_of_the_triangle}")

side_a = 5
side_b = 4
side_c = 3
perimeter_of_the_triangle = 12
side_a = input("¿cual es el lado a?")
print(f"el lado a es {side_a}")
side_b = input("¿cual es el lado b?")
print(f"el lado b es {side_b}")
side_c = input("¿cual es el lado c?")
print(f"el lado c es {side_c}")
perimeter_of_the_triangle = side_a + side_b + side_c
perimeter_of_the_triangle = imput("¿cual es el peimetro?")
print(f"el perimetro es {perimeter_of_the_triangle}")

length = input("¿cual es el largo del rectangulo?")
print(f"el largo del rectangulo es {length}")
width = input("¿cual es la altura del rectangulo?")
print(f"la altura del rectangulo es {width}")
area_of_the_rectangle = length * width
area_of_the_rectangle = input("¿cual es area del rectangulo?")
print(f"el area del rectangulo es {area_of_the_rectangle}")
perimeter_of_the_rectangle = 2 * (length + width)
perimeter_of_the_rectangle = input("¿cual es el perimetro del rectangulo?")
print(f"el perimetro del rectangulo es {perimeter_of_the_rectangle}")

pi = 3.14 
radius = input("¿cual es el radio del circulo?")
print(f"el radio del circulo es {radius}")
area_of_a_circle = pi * radius * radius
area_of_a_circle = input("¿cual es el area del circulo?")
print(f"el area del criculo es {area_of_a_circle}")
circumference = 2 * pi * radius
circumference = input("¿cual es la circunferencia del circulo?")
print(f"la circunferencia es {circumference}")

funcion1 = "y = 2x - 2"
print("su funcion es:{funcion1}")
pendientef1=str(2)
print("su pendiente es:{pendientef1}" )
interceptx=2*0 -2
print("el intercepto de x es:{interceptx}")
intercepty=(2+0)/2
print("el intercepto de y es: {intercepty}")

punto1 = (2,2)
punto2 = (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = (y2-y1)/(x2-x1)
print("su pendiente es: {m}")
euclideandistance= (x2-x1)**2 + (y2-y1)**2
print(f"la distancia eucliana es de: {euclideandistance}")

print(pendientef1==m)

numeros_prueba= (2, -3, 4, 5, 6)
for n in numeros_prueba:
    print(n**2 + 6*n +9)
