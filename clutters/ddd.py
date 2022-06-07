from sympy.abc import x, A,B
from sympy.abc import y
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy import Function
import sympy as sp
import inspect


# x,y,z = sp.symbols("x y z")# expr = -y + 3*x
# expr.subs(x,1)

# expr = -y ** 2 + x ** 3 - 3 * x + 3
# exprr = sp.cos(x) + 1+x
# x=2
# exprr.subs(+x, 2) # cos(y)+1

# eq = sp.Eq(expr, 0)
# # eq.subs(x, 1)
# x= 1
# y = sp.symbols("y")
# equation = sp.Eq( -y ** 2 + x ** 3 - 3 * x + 3,0)
# result= sp.solve(equation)
# # print(exprr)
# # print(type(exprr))
# print(result)
my_lam = lambda x,y : 5*x + 3*y
# lambda x, y: -y ** 2 + x ** 3 - 3 * x + 3
# G = 8*A*B # now this is a symbolic expression, not a string
# H = lambdify( [A,B], G, "numpy" )
# print(H(1,1))

func = lambda x,y: y ** 2 + x ** 2 - 5
funcString = str(inspect.getsourcelines(func)[0])
funcString = funcString.strip("['\\n']").split(" = ")[1]
A = sp.sympify(funcString.split(":")[1])
# x = sympy.symbols("x")
# f = lambdify(Function('f'), my_lam)
# A = sp.sympify("  y ** 2 + x ** 2 - 5")
# A=  y ** 2 + x ** 2 - 5
A=A.subs(x,2)
EQ = sp.Eq(A, 0)
result=sp.solve(EQ)
print(result)
print(type(float(result[0])))
result = float(result[0])

# print(A)

# lam_f = lambdify([x,y],A)

# print(result)
# print(lam_f(4,2))

# print(lambda x : 5*x)
# print(type(lambda x : 5*x))

