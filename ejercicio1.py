#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from gmes.geometry import Cartesian
from gmes.material import DcpPlrc, DcpAde, DrudePole, CriticalPoint
from gmes.constant import c0

class Oro(DcpAde):
    def __init__(self, a):
        dp1 = DrudePole(omega=1.31839e16 * a / c0, gamma=1.09173e14 * a / c0)
        cp1 = CriticalPoint(amp=0.273222, phi=-1.18299, omega=3.88123e15 * a / c0, gamma=4.52006e14 * a / c0)
        cp2 = CriticalPoint(amp=3.04155, phi=-1.09115, omega=4.20737e15 * a / c0, gamma=2.35409e15 * a / c0)
        DcpAde.__init__(self, eps_inf=1.11683, mu_inf=1, sigma=0, dps=(dp1,), cps=(cp1, cp2))

class Plata(DcpPlrc):
    def __init__(self, a):
        dp1 = DrudePole(omega=1.38737e16 * a / c0, gamma=2.07331e13 * a / c0)
        cp1 = CriticalPoint(amp=1.3735, phi=-0.504658, omega=7.59914e15 * a / c0, gamma=4.28431e15 * a / c0)
        cp2 = CriticalPoint(amp=0.304478, phi=-1.48944, omega=6.15009e15 * a / c0, gamma=6.59262e14 * a / c0)
        DcpPlrc.__init__(self, eps_inf=0.89583, mu_inf=1, sigma=0, dps=(dp1,), cps=(cp1, cp2))

def seleccionar_material():
    while True:
        print("Selecciona el material:")
        print("1. Oro")
        print("2. Plata")
        eleccion = input("Ingresa tu elección: ")
        if eleccion == '1':
            return Oro
        elif eleccion == '2':
            return Plata
        else:
            print("Elección inválida")

def seleccionar_ecuacion():
    print("Selecciona la ecuación de Maxwell a utilizar:")
    print("1. Ley de Faraday (curl E = -dB/dt)")
    print("2. Ley de Ampere (curl H = J + dD/dt)")
    print("3. Ley de Gauss para la electricidad (div D = ρ)")
    print("4. Ley de Gauss para el magnetismo (div B = 0)")
    while True:
        eleccion = input("Ingresa tu elección: ")
        if eleccion in {'1', '2', '3', '4'}:
            return eleccion
        else:
            print("Elección inválida")

def obtener_variables_usuario(ecuacion_elegida):
    if ecuacion_elegida == '1':
        E = np.array(input("Ingresa el campo eléctrico E (como valores separados por comas): ").split(), dtype=float)
        B = np.array(input("Ingresa la densidad de flujo magnético B (como valores separados por comas): ").split(), dtype=float)
        return E, B
    elif ecuacion_elegida == '2':
        H = np.array(input("Ingresa el campo magnético H (como valores separados por comas): ").split(), dtype=float)
        J = np.array(input("Ingresa la densidad de corriente J (como valores separados por comas): ").split(), dtype=float)
        D = np.array(input("Ingresa el campo de desplazamiento eléctrico D (como valores separados por comas): ").split(), dtype=float)
        return H, J, D
    elif ecuacion_elegida == '3':
        D = np.array(input("Ingresa el campo de desplazamiento eléctrico D (como valores separados por comas): ").split(), dtype=float)
        rho = float(input("Ingresa la densidad de carga ρ: "))
        return D, rho
    elif ecuacion_elegida == '4':
        B = np.array(input("Ingresa la densidad de flujo magnético B (como valores separados por comas): ").split(), dtype=float)
        return B
    else:
        print("Elección inválida")
        sys.exit()

def aplicar_ecuacion_maxwell(ecuacion_elegida, variables):
    if ecuacion_elegida == '1':
        E, B = variables
        curl_E = np.cross(E, B)
        print("curl E =", curl_E)
    elif ecuacion_elegida == '2':
        H, J, D = variables
        curl_H = np.cross(H, J) + np.gradient(D)
        print("curl H =", curl_H)
    elif ecuacion_elegida == '3':
        D, rho = variables
        div_D = np.div(D)
        print("div D =", div_D, "ρ =", rho)
    elif ecuacion_elegida == '4':
        B = variables
        div_B = np.div(B)
        print("div B =", div_B)
    else:
        print("Elección inválida")
        sys.exit()

def main():
    material = seleccionar_material()()
    ecuacion_elegida = seleccionar_ecuacion()
    variables = obtener_variables_usuario(ecuacion_elegida)
    aplicar_ecuacion_maxwell(ecuacion_elegida, variables)

if __name__ == "__main__":
    main()

