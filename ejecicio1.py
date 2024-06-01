# -*- coding: utf-8 -*-

import numpy as np
from gmes.material import Material
from gmes.geometry import Cartesian

class MaxwellSolver:
    def __init__(self, material, geometry):
        self.material = material
        self.geometry = geometry

    def solve_gauss_law(self):
        epsilon_0 = self.material.epsilon_0
        rho = float(input("Ingrese el valor de ρ (carga volumétrica): "))
        return rho / epsilon_0

    def solve_gauss_law_magnetism(self):
        mu_0 = self.material.mu_0
        J = float(input("Ingrese el valor de J (densidad de corriente): "))
        return J * mu_0

    def solve_faradays_law(self):
        dPhi_dt = float(input("Ingrese el valor de dΦ/dt (tasa de cambio del flujo magnético): "))
        return -dPhi_dt

    def solve_amperes_law(self):
        mu_0 = self.material.mu_0
        J = float(input("Ingrese el valor de J (densidad de corriente): "))
        sigma = self.material.sigma
        E = float(input("Ingrese el valor de E (campo eléctrico): "))
        return mu_0 * J + sigma * E

if __name__ == "__main__":
    material = Material()
    geometry = Cartesian((10, 10, 10))

    solver = MaxwellSolver(material, geometry)

    print("Elige qué ecuación de Maxwell quieres resolver:")
    print("1. Ley de Gauss (div E = ρ / ε_0)")
    print("2. Ley de Gauss para el Magnetismo (div B = μ_0 * J)")
    print("3. Ley de Faraday (curl E = -dΦ/dt)")
    print("4. Ley de Ampère (curl B = μ_0 * J + σ * E)")

    ecuacion = input("Ingresa tu elección (1-4): ")
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

