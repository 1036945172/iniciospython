mensaje = "        Bienvenido.... al curso de python"

#metodo len, imprime el tamaño de longitud del string
print("El tamaño del texto original es de: ",len(mensaje))

#strip, quita espacios al inicio y al final
sinEspacios =mensaje.strip()

print("El tamaño del texto es de: ",(sinEspacios))
print("El tamano del texto sin espacios es: ",len(sinEspacios))

#upper es para comvertir los textos en mayuscula
print("Texto en MAYUSCULA sostenida")
print(sinEspacios.upper())
#lower es para convertir los textos en minusculas
print(sinEspacios.lower())
#title es para poner la letra inicial en mayuscula de cada texto
print(sinEspacios.title())
#capitalize es para poner solo la primera letra mayuscula
print(sinEspacios.capitalize())

parrafo = sinEspacios.split("...")
print(parrafo[0])
print(parrafo[1])



