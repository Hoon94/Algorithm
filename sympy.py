import numpy as np
import sympy as sym  # symbolic python
from sympy.abc import x


def func(val):
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x, val), fun


def func_gradient(fun, val):
    _, function = fun(val)
    diff = sym.diff(function, x)
    return diff.subs(x, val), diff


def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(fun, init_point)
    while np.abs(diff) > epsilon:
        val = val - lr_rate*diff
        diff, _ = func_gradient(fun, val)
        cnt += 1

    print("함수: {}, 연산횟수: {}, 최소점: ({}, {})".format(
        fun(val)[1], cnt, val, fun(val)[0]))


gradient_descent(fun=func, init_point=np.random.uniform(-2, 2))

# 함수: Poly(x**2 + 2*x + 3, x, domain='ZZ'), 연산횟수: 460, 최소점: (-0.999995059315067, 2.00000000002441)
