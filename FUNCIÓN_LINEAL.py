import numpy as np
import matplotlib .pyplot as mpl

## Funcion que simula la senal
def senal(ts):
    x=[]
    for t in ts:
        x.append(t)
    return x


## Esta es nuestra funcion principal
def main(ini ,fin ,delta):
    ts =np.arange(ini ,fin ,delta)
    x=senal(ts)
    mpl.plot(ts ,x)
    mpl.grid ()
    mpl.title('Señal simulada ')
    mpl.xlabel("Tiempo ")
    mpl.ylabel("Volts")
    mpl.savefig("figEj1.png", format='png', dpi=300)
    mpl.show ()  
    
## Este es el punto de entrada al programa
if __name__ == "__main__":
    main(0, 10, 0.1)