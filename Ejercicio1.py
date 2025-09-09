edad = 18
nombre = "Lucas"
tiene_lnc = True

if edad >= 18:
    print(nombre, "es mayor de edad.")


if edad >= 18:
    if tiene_lnc:
        print(nombre, "puede manejar porque es mayor y tiene licencia nacional de conducir.")
    else:
        print(nombre, "es mayor de edad pero no tiene licencia nacional de conducir.")
else:
    print(nombre, "es menor de edad.")