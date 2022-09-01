from auto.motor import Motor
from auto.auto import Auto


print("consecionario CoderHouse :D")

print('Opciones (1: Construir motor, 2: Fabricar auto, 3: Comprar Auto)')
opcion = int (input('Opcion: '))

if opcion == 1 :
    codigoMotor = input("codigo de motor: ")
    nombreMotor = input("nombre de motor: ")

    tipoCombustible= input("Tipo de conbustrible: ")
    cilindrada = input ("cilindrada: ")
    potencia= input ("potencia: ")
    torque= input ("torque: ")
    
    newMotor = Motor(tipoCombustible,cilindrada,potencia,torque)
    newMotor.setfabricarMotor(codigoMotor,nombreMotor)

elif opcion == 2:

    codigoAuto = input("codigo de auto: ")
    nombreAuto = input("nombre de auto: ")
   

    ruedas = input ("cantidad de puertas: ")
    puertas = input ("cantida de ruedas: ")
    tipo = input ("tipo de autos: ")

    newAuto = Auto(ruedas, puertas, tipo)
    newAuto.getlistaMotores()
    
    codigoMotor = input("codigo de motor: ")
    newAuto.setfabricarAuto(codigoAuto,nombreAuto,codigoMotor)

elif opcion == 3:

    newAuto = Auto()
    newAuto.getlistarAutos()

    codigoAuto = input("Codigo de Auto: ")
    
    print(newAuto.getcomprarAuto(codigoAuto))
    
    

