import numpy as np
import sympy as sp
import math

def find_cost(z, x_vector):
    subs_dict = {ind_var[i]: x_vector[i] for i in range(len(ind_var))}
    cost = z.subs(subs_dict)
    return cost


def substitute(g, x_vector):
    subs_dict = {ind_var[i]: x_vector[i] for i in range(len(ind_var))}
    substituted_g = np.array([expr.subs(subs_dict) for expr in g])
    return substituted_g

"""Initializing values of g, ⍺, ε"""

x, y = sp.symbols("x y")
ind_var = ['x', 'y']

Z = x**2 + y + 3

g = []

for i in ind_var:
    var_dash = sp.Derivative(Z, i)
    g.append(var_dash.doit())

g = np.array(g)
alpha = 0.1
epsilon = 0.01
x = np.array([0, 0])

subs_dict = {ind_var[i]: x[i] for i in range(len(ind_var))}
cost = Z.subs(subs_dict)

"""Minimization"""
while(cost > epsilon):
    
