from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

from qiskit_nature.second_q.algorithms import GroundStateEigensolver, NumPyMinimumEigensolverFactory
from qiskit_nature.second_q.mappers import JordanWignerMapper, QubitConverter

driver = PySCFDriver(
    atom="H 0 0 0; H 0 0 0.735",
    basis="sto3g",
    charge=0,
    spin=0,
    unit=DistanceUnit.ANGSTROM,
)


problem = driver.run()
print(problem)
    

hamiltonian = problem.hamiltonian

coefficients = hamiltonian.electronic_integrals
print(coefficients.alpha)


second_q_op = hamiltonian.second_q_op()
print(second_q_op)

repulsion_energy = hamiltonian.nuclear_repulsion_energy
print(repulsion_energy)

print(problem.molecule)

print(problem.reference_energy)

print(problem.num_particles)

print(problem.num_spatial_orbitals)

print(problem.basis)


solver = GroundStateEigensolver(
    QubitConverter(JordanWignerMapper()),
    NumPyMinimumEigensolverFactory(),
)

result = solver.solve(problem)
print(result)
