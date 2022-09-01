class Motor:
    def __init__(self,tipoCombustible=None, cilindrada=None, potencia=None, torque=None):
        self.tipoCombustible= tipoCombustible
        self.cilindrada= cilindrada
        self.potencia= potencia
        self.torque= torque
        
    def setfabricarMotor(self, codigoMotor, nombreMotor):
        with open('auto/recursos/listaMotores.txt', 'a') as newMotor:
            data = f'{codigoMotor}|{nombreMotor}|{self.tipoCombustible}|{self.cilindrada}|{self.potencia}|{self.torque}\n'
            newMotor.write(data)
            newMotor.close()
        return True

    def getobtenerMotor(self, codigoMotor):
        with open ('auto/recursos/listaMotores.txt', 'r') as Motores:
            for Motor in Motores:
                detalles = Motor.split("|")
                if codigoMotor == detalles [0]:
                    Motores.close()
                    return detalles
            else:
                Motores.close()
                return False
    def getlistaMotores(self):
        with open('./auto/recursos/listaMotores.txt' , 'r') as Motores:
            for Motor in Motores:
                print(Motor)