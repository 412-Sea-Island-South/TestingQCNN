from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.reset(qreg_q[0])
circuit.reset(qreg_q[1])
circuit.reset(qreg_q[2])
circuit.rz(pi/2, qreg_q[2])
circuit.sx(qreg_q[2])
circuit.rz(pi/2, qreg_q[2])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.rz(-pi/4, qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.rz(pi/4, qreg_q[2])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.rz(pi/4, qreg_q[1])
circuit.rz(-pi/4, qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.rz(pi/4, qreg_q[2])
circuit.barrier(qreg_q[0])
circuit.barrier(qreg_q[1])
circuit.rz(pi/2, qreg_q[2])
circuit.barrier(qreg_q[0])
circuit.barrier(qreg_q[1])
circuit.sx(qreg_q[2])
circuit.rz(pi/4, qreg_q[0])
circuit.rz(-pi/4, qreg_q[1])
circuit.rz(pi/2, qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])

#A convoluted way to do
#circuit.mct(qreg_q[0], qreg_q[1], qreg_q[2])