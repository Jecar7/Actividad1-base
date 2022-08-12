print("""
    1) Punto 1      3) punto 3
    2) Punto 2        4) Mas...
    """)


eligio=input("-Selecciona algo :")

if eligio=="1":
    
     num1 = int(input("dijite el numero 1:|" ))
     num2 = int(input("dijite el numero 2:|" ))
     num3 = int(input("dijite el numero 3:|" ))
     if num1>num2 and num2>num3:
        print(num1)
        print(num2)
        print(num3)
     elif num1>num3 and num3>num2:
        print(num1)
        print(num3)
        print(num2)
     elif num2>num1 and num1>num3:
        print(num2)
        print(num1)
        print(num3)    
     elif num2>num3 and num3>num1:
        print(num2)
        print(num3)
        print(num1)
     elif num2>num3 and num3>num1:
        print(num2)
        print(num3)
        print(num1)   
    
if eligio=="2":
    x = 3
    y = 5
    print("x * y = ", x * y)
if eligio=="3":
    print("Creo que hace frío")
if eligio=="4":
    print("otra opción")
    