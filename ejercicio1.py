# -*- coding: utf-8 -*-

import gmes
import numpy as np

class MaxwellEquationsSolver:
    def __init__(self):
        pass

    def resolver_gauss_para_e(self, charge_density):
        solver = gmes.GaussForElectricFieldSolver()
        solver.charge_density = charge_density
        solver.solve()
        return solver.get_electric_field()

    def resolver_gauss_para_b(self, charge_density):
        solver = gmes.GaussForMagneticFieldSolver()
        solver.charge_density = charge_density
        solver.solve()
        return solver.get_magnetic_field()

    def resolver_faraday(self, magnetic_field_variation):
        solver = gmes.FaradaySolver()
        solver.magnetic_field_variation = magnetic_field_variation
        solver.solve()
        return solver.get_induced_electric_field()

    def resolver_ampere_maxwell(self, current_density):
        solver = gmes.AmpereMaxwellSolver()
        solver.current_density = current_density
        solver.solve()
        return solver.get_magnetic_field()

if __name__ == "__main__":
    solver = MaxwellEquationsSolver()

    print("Ecuaciones disponibles:")
    print("1. Gauss para E")
    print("2. Gauss para B")
    print("3. Faraday")
    print("4. Ampere-Maxwell")

    opcion = int(input("Seleccione el número de la ecuación que desea resolver: "))

    if opcion == 1:
        charge_density = float(input("Densidad de carga (C/m^3): "))
        resultado = solver.resolver_gauss_para_e(charge_density)
    elif opcion == 2:
        charge_density = float(input("Densidad de carga (C/m^3): "))
        resultado = solver.resolver_gauss_para_b(charge_density)
    elif opcion == 3:
        magnetic_field_variation = float(input("Variación del campo magnético (T/s): "))
        resultado = solver.resolver_faraday(magnetic_field_variation)
    elif opcion == 4:
        current_density = float(input("Densidad de corriente (A/m^2): "))
        resultado = solver.resolver_ampere_maxwell(current_density)
    else:
        print("Opción no válida")

    print("Resultado:", resultado)

