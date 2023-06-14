import numpy as np
import random

def write_float (self, value):
    precision = self.float_precision # sig figs - 1
    m, e = (f"%.{precision}e" % np.abs(value)) .split("e")
    i, f = m.split (".")
    i = i + f
    ipart = int (i)
    expon = int(e) - precision
    if expon < -100:
        ipart = 0
    if ipart == 0:
        value = 0.0
        expon = 0
    res = ["+"] if value >= 0.0 else ["-"]
    res = res + [str (ipart)]
    return res + ["E" + str (expon) ]

def encode (self, vect, cplx=False):
    lst = []
    l = len (vect)
    lst.append("V" + str (1))
    for val in vect:
        if cplx:
            lst.extend(self.write_float(val.real))
            lst.extend(self.write_float(val.imag))
        else:
            lst.extend(self.write_float(val))
    return lst

def generate(self, rng) :
    degree = rng.randint(self.min_degree, self.max_degree + 1)
    roots = rng.rand(degree) * self.max_root
    roots = roots.astype(complex)
    for i in range(degree//2):
        cplex = (rng.rand() < self.prob_complex)
        if cplex:
            roots[2 * i] = complex(roots[2 * i], roots[2 * i + 1])
            roots [2 * i + 1] = np.conj(roots[2 * i])
    poly = np.real (np.poly (roots))
    if self.sort_roots:
        roots = np.sort
    complex (roots)