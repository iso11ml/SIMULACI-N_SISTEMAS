import numpy as np
import matplotlib .pyplot as mpl


def escalon (ts,a,k): 
    x=[]
    for t in ts:
        if t<k:
            x.append (0)
        else:
            x.append(a)
    return x

## Esta es nuestra funcion principal
def main(ini ,fin ,delta):
    ts = np.arange(ini ,fin ,delta) # Rango de valores para incializar el arreglo
    x1= escalon (ts ,10 ,5)
    x2= escalon (ts ,1 ,0)
    mpl.plot(ts ,x1)
    mpl.plot(ts ,x2)
    mpl.grid ()
    mpl.title('ESCALON NORMAL Y ESCALON CON DESFASE')
    mpl.xlabel('Tiempo ')
    mpl.ylabel('Respuesta ')
    mpl. savefig ('figEj2.png',format ='png',dpi =300)
    mpl.show ()

## Este es el punto de entrada al programa
if __name__ == "__main__":
    main(-10, 10, 0.1)