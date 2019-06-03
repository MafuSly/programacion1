def log(mensaje):
    print("::" + mensaje)

def logPez(pez):
    print(" Ejes X=[" +str(posX(pez))+ "] Y=[" +str(posY(pez))+ "]:: Velocidad X=["+str(velX(pez))+"] Y=["+str(velY(pez))+"]")




def posX(pez):
    return pez[0][0]

def posY(pez):
    return pez[0][1]

def velX(pez):
    return pez[1][0]

def velY(pez):
    return pez[1][1]


