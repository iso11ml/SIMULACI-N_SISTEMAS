import numpy as np
import matplotlib .pyplot as mpl

def rampa(ts ,a,k):
    x=[]
    for t in ts:
        x.append(a*(t-k))
    return x

def main(ini ,fin ,delta):
    ts=np.arange(ini ,fin ,delta)
    x1=rampa(ts ,1 ,0)
    x2=rampa(ts ,1 ,3)
    mpl.plot(ts ,x1)
    mpl.plot(ts ,x2)
    mpl.grid ()
    mpl.title('RAMPA NORMAL Y RAMPA CHIDA ')
    mpl.xlabel('Tiempo ')
    mpl.ylabel('Resspuesta ')
    mpl. savefig ('FigEj3.png',format ='png',dpi =300)
    mpl.show ()

if __name__ == "__main__":
    main(0, 10, 0.1)