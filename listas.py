modulos=["Logica","Base de Datos","HTML5","Nuevas Tecnologias"]

print(modulos)
print("El elemneto de la posicion 0 es ---->: ", modulos[0])
print("El ultimo elemento de la lista es ---->: ",modulos[-1])
print("Numero de elementos que tiene la lista es -->: ",len(modulos))
print("Ultimo elemento de la lista es: ------->",modulos[len(modulos)-1])

#append sirve para agregar un elemento al final
print("Agregar un elemto a lista ... Metologias Agiles ")
modulos.append("Metologias Agiles")
print(modulos)

#inser sirve para poner posicion a un elemento que agregue a la lista
modulos.insert( 1,"HTML5")
print(modulos)

#count sirve para que me diga cuantas veces se repite algun elemento de la lista
print("Las veces que se repite HTML5 es:--->",modulos.count("HTML5"))

#sort me sirve para que me ordene la lista en orden alfabeticamente
print("Lista ordenada alfabeticamente")
modulos.sort()
print(modulos)
i=1
for indice in modulos:
    print(i,indice)
    i=i+1