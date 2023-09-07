print("Calcular las notas definitivas")
Nombre=input("Nombre Estudiante:")
nota1=float(input("Digite nota 1:"))
nota2=float(input("Digite nota 2:"))
nota3=float(input("Digite nota 3:"))
definitiva=(nota1+nota2+nota3)/3
#print("Nombre: ",Nombre, ", Su nota final es",definitiva)
print(f"Nombre: {Nombre}\n Su nota final es {definitiva}")

if definitiva>=0 and definitiva <=2:
    print ("El estudiante", Nombre,"tiene una calificacion de ", definitiva,"Tienes problemas de atencion")
elif definitiva>=2.1 and definitiva<=3:
    print ("El estudiante", Nombre,"tiene una calificacion de ", definitiva,"Puede recuperar")
    if definitiva>3 and definitiva<=4:
        print ("El estudiante", Nombre,"tiene una calificacion de ", definitiva,"Muy bien, gano")
    elif definitiva>=4 and definitiva<=4.6:
        print ("El estudiante", Nombre,"tiene una calificacion de ", definitiva,"Eres genial")
        if definitiva>4.6:
            print ("El estudiante", Nombre,"tiene una calificacion de ", definitiva,"Eres el mejor")
        else:
        
            print("Error")
    
        
