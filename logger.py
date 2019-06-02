def log(mensaje):
    print("::" + mensaje)

def logPez(pez):
    print(" Ejes X=[" +str(posX(pez))+ "] Y=[" +str(pez[0][1])+ "]:: Velocidad X=["+str(pez[1][0])+"] Y=["+str(pez[1][1])+"]")


def posX(pez):
    return pez[0][0]

def posY(pez):
    return pez[0][1]
