print("""
    1) Herramientas       3) Temperatura
    2) Calculadora        4) Mas...
    """)

# Leemos lo que ingresa el usuario
eligio=input("-Selecciona algo :")

# Según lo que ingresó, código diferente
if eligio=="1":
    print("Listamos otras herramientas")
elif eligio=="2":
    x = 3
    y = 5
    print("x * y = ", x * y)
elif eligio=="3":
    print("Creo que hace frío")
elif eligio=="4":
    print("otra opción")
else:
    print("Opción no válida")