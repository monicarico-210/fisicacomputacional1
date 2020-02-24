
print("Escriba un código que calcule la posición en J para un objeto en caida libre, luego de un tiempo t y una altura inicial h; ambos valores ingresados por consola.")


h=float(input("digite el valor de h:"))
t=float(input("digite el tiempo que se demora en caer:"))
g=9.8
y=h+0.5*g*t**2
print("la altura es:",y)

