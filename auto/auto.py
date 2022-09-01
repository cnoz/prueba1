from auto.motor import Motor

class Auto(Motor):
    def __init__ (self, ruedas=None, puertas=None, tipo=None):
        self.ruedas= ruedas
        self.puertas= puertas
        self.tipo= tipo
        
    def setfabricarAuto(self, codigoAuto, nombreAuto, codigoMotor):
        with open ('./auto/recursos/listaAutos.txt', 'a') as newAuto:
            data = f'{codigoAuto}|{nombreAuto}|{self.tipo}|{self.ruedas}|{self.puertas}|{codigoMotor}\n'
            newAuto.write(data)
            newAuto.close()

    def getcomprarAuto(self,codigoAuto):
        with open('./auto/recursos/listaAutos.txt', 'r') as Autos:
            for auto in Autos:
                detalles = auto.split("|")
                if codigoAuto == detalles[0]:
                    Autos.close()
                    return(f"Has comprado un {detalles[1]}.")
            else:
                return False


    def getlistarAutos(sefl):
        with open('./auto/recursos/listaAutos.txt', 'r') as Autos:
            for auto in Autos:
                print(auto)  
                  

