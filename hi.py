import turtle

t=turtle.Pen()

def estrella(tamano,n):
    if n%2==0:
        ang=(360/n)+180

    else:
        ang=(-(360/n+180)*2)

    for x in range(n):
        t.forward(tamano)
        t.left(ang)
    
tamano=int(input("INGRESE EL TAMAÑO DE LOS LADOS: "))
n=int(input("INGRESE UN NUMERO DE LADOS: "))


estrella(tamano,n)
