# -*- coding: utf-8 -*-
import numpy as np
from gmes.material import Material
from gmes.geometry import Cartesian

class MaxwellSolver:
    def __init__(self, material, geometry):
        self.material = material
        self.geometry = geometry

    def solve_gauss_law(self):
        # Asignar un valor predeterminado si epsilon_0 no está presente
        epsilon_0 = getattr(self.material, 'epsilon_0', 8.854e-12) # Valor predeterminado de la permitividad del vacío
        rho = float(raw_input("Ingrese el valor de ρ (carga volumétrica): "))
        return rho / epsilon_0

    def solve_gauss_law_magnetism(self):
        # Asignar un valor predeterminado si mu_0 no está presente
        mu_0 = getattr(self.material, 'mu_0', 4 * np.pi * 1e-7) # Valor predeterminado de la permeabilidad del vacío
        J = float(raw_input("Ingrese el valor de J (densidad de corriente): "))
        return J * mu_0

    def solve_faradays_law(self):
        dPhi_dt = float(raw_input("Ingrese el valor de dΦ/dt (tasa de cambio del flujo magnético): "))
        return -dPhi_dt

    def solve_amperes_law(self):
        # Asignar un valor predeterminado si mu_0 no está presente
        mu_0 = getattr(self.material, 'mu_0', 4 * np.pi * 1e-7) # Valor predeterminado de la permeabilidad del vacío
        J = float(raw_input("Ingrese el valor de J (densidad de corriente): "))
        sigma = getattr(self.material, 'sigma', 0) # Valor predeterminado de la conductividad (0 si no se proporciona)
        E = float(raw_input("Ingrese el valor de E (campo eléctrico): "))
        return mu_0 * J + sigma * E

if __name__ == "__main__":
    # Creando una instancia de Material con valores predeterminados
    material = Material()
    geometry = Cartesian((10, 10, 10))

    solver = MaxwellSolver(material, geometry)

    print("Elige qué ecuación de Maxwell quieres resolver:")
    print("1. Ley de Gauss (div E = ρ / ε_0)")
    print("2. Ley de Gauss para el Magnetismo (div B = μ_0 * J)")
    print("3. Ley de Faraday (curl E = -dΦ/dt)")
    print("4. Ley de Ampère (curl B = μ_0 * J + σ * E)")

    ecuacion = raw_input("Ingresa tu elección (1-4): ")
    print("Has seleccionado:", ecuacion)  # Agregamos este mensaje de depuración
    resultado = None

    if ecuacion == "1":
        resultado = solver.solve_gauss_law()
    elif ecuacion == "2":
        resultado = solver.solve_gauss_law_magnetism()
    elif ecuacion == "3":
        resultado = solver.solve_faradays_law()
    elif ecuacion == "4":
        resultado = solver.solve_amperes_law()
    else:
        print("Selección de ecuación inválida")
    
    if resultado is not None:
        print("Resultado de resolver la ecuación {}: {}".format(ecuacion, resultado))
