import numpy as np
import matplotlib.pyplot as mpl

# Esta función genera una señal senoidal
def seno(ts, a, f, theta):
    x = []
    for t in ts:
        x.append(a * np.sin((2 * np.pi * f * t) + theta))
    return x

# Esta función genera una señal cosenoidal
def coseno(ts, a, f, theta):
    x = []
    for t in ts:
        x.append(a * np.cos((2 * np.pi * f * t) + theta))
    return x

# Esta es la función principal del programa
def main(ini, fin, delta):
    ts = np.arange(ini, fin, delta)
    x1 = seno(ts, 10, 0.25, 0)
    x2 = coseno(ts, 20, 0.125, np.pi / 2)
    mpl.plot(ts, x1, label=r'$10\sin (\omega_1 t)$')
    mpl.plot(ts, x2, label=r'$20\sin (\omega_2 t+\pi/2)$')
    mpl.grid()
    mpl.title('SEÑAL SENO  Y COSENO')
    mpl.xlabel('Tiempo')
    mpl.ylabel('Respuesta')
    mpl.legend()
    mpl.savefig('FigEj6.png', format='png', dpi=300)
    mpl.show()

# Este es el punto de entrada al programa
if __name__ == '__main__':
    main(-5, 15, 0.1)
