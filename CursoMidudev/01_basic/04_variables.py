#Para asingaer varibales solo es necesario poner nombre = valor
my_name = "Emerson"
print(my_name)

age = 32
print(age)
age = 39 #Se pueden reasignar
print(age)

#Python es de Tipado diinamico: es el tipo de dato se determina en tiempo de ejecucion, que no tiene que declarrlo explicicamente

name = "EMerson"
print(type(name))
#Python es de tpiado fuerte: python no realiza conversiones automaticamente

#f-string 
print(f"hola {name}, tengo {age + 8} años")


#No recomendada forma de asignar variables
name, age, city = "emerson", 32, "Guatemala"

#Convenciones de nombres de variables
mi_nombre_de_variable = "ok"
MiNombreDeVariable = "KO" #PascalCase

mi_nombre_de_variable_123 = "ok"

#SImular constante todo en mayuscula, UPPER_CASE 
MI_CONSTANTE = 3.14
print(MI_CONSTANTE)

#TIPADO DE VARIABLES


is_user_logged_in:bool = True
