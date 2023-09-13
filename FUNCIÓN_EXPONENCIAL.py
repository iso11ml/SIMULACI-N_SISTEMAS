import numpy as np
import math
import matplotlib .pyplot as mpl

# Esta es la funcion que simula un exponencial
def expo(ts ,alpha ,a,k):
    x=[]
    for t in ts:
        if t<k:
            x.append (0)
        else:
            x.append(a*math.exp(alpha *(t-k)))
    return x

# Esta es la funcion prinicpal del programa
def main(ini ,fin ,delta):
    ts=np.arange(ini ,fin ,delta)
    x1=expo(ts , -2 ,10 ,0)
    x2=expo(ts , -2 ,10 ,3)
    x3=expo(ts ,-4,8,-3)
    mpl.plot(ts ,x1 ,ts ,x2 ,ts ,x3)
    mpl.grid ()
    mpl.title('UN ESCALON NORMAL , OTRO CHIDO Y OTRO NO TAN CHIDO ')
    mpl.xlabel('Tiempo ')
    mpl.ylabel('Respuesta ')
    mpl.legend ((r'$10e ^{-2t}$',r'$10e ^{ -2(t -3)}$',r'$8e ^{ -4(t+3)}$'))
    mpl. savefig ('FigEj4.png',format ='png',dpi =300)
    mpl.show ()

## Punto de entrada al programa
if __name__ =='__main__':
    main ( -10 ,10 ,0.1)