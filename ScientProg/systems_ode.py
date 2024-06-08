"""Computes the runge kutta method for solving liner ODEs"""

import numpy as np
from numpy import exp, linspace


def runge_kutta_system(u1, u2, u3, a, b, h, u10, u20, u30):
    """Solves a system of ODEs using the Runge Kutta Method"""
    t = linspace(a, b, int((b - a) / h) + 1)
    u1_val = np.zeros_like(t)
    u2_val = np.zeros_like(t)
    u3_val = np.zeros_like(t)
    u1_val[0] = u10
    u2_val[0] = u20
    u3_val[0] = u30

    for i in range(1, len(t)):
        k1_u1 = h * u1(t[i - 1], u1_val[i - 1], u2_val[i - 1], u3_val[i - 1])
        k1_u2 = h * u2(t[i - 1], u1_val[i - 1], u2_val[i - 1], u3_val[i - 1])
        k1_u3 = h * u3(t[i - 1], u1_val[i - 1], u2_val[i - 1], u3_val[i - 1])

        k2_u1 = h * u1(
            t[i - 1] + h / 2,
            u1_val[i - 1] + k1_u1 / 2,
            u2_val[i - 1] + k1_u2 / 2,
            u3_val[i - 1] + k1_u3 / 2,
        )
        k2_u2 = h * u2(
            t[i - 1] + h / 2,
            u1_val[i - 1] + k1_u1 / 2,
            u2_val[i - 1] + k1_u2 / 2,
            u3_val[i - 1] + k1_u3 / 2,
        )
        k2_u3 = h * u3(
            t[i - 1] + h / 2,
            u1_val[i - 1] + k1_u1 / 2,
            u2_val[i - 1] + k1_u2 / 2,
            u3_val[i - 1] + k1_u3 / 2,
        )

        k3_u1 = h * u1(
            t[i - 1] + h / 2,
            u1_val[i - 1] + k2_u1 / 2,
            u2_val[i - 1] + k2_u2 / 2,
            u3_val[i - 1] + k2_u3 / 2,
        )
        k3_u2 = h * u2(
            t[i - 1] + h / 2,
            u1_val[i - 1] + k2_u1 / 2,
            u2_val[i - 1] + k2_u2 / 2,
            u3_val[i - 1] + k2_u3 / 2,
        )
        k3_u3 = h * u3(
            t[i - 1] + h / 2,
            u1_val[i - 1] + k2_u1 / 2,
            u2_val[i - 1] + k2_u2 / 2,
            u3_val[i - 1] + k2_u3 / 2,
        )

        k4_u1 = h * u1(
            t[i - 1] + h,
            u1_val[i - 1] + k3_u1,
            u2_val[i - 1] + k3_u2,
            u3_val[i - 1] + k3_u3,
        )
        k4_u2 = h * u2(
            t[i - 1] + h,
            u1_val[i - 1] + k3_u1,
            u2_val[i - 1] + k3_u2,
            u3_val[i - 1] + k3_u3,
        )
        k4_u3 = h * u3(
            t[i - 1] + h,
            u1_val[i - 1] + k3_u1,
            u2_val[i - 1] + k3_u2,
            u3_val[i - 1] + k3_u3,
        )

        u1_val[i] = u1_val[i - 1] + (1 / 6) * (k1_u1 + 2 * k2_u1 + 2 * k3_u1 + k4_u1)
        u2_val[i] = u2_val[i - 1] + (1 / 6) * (k1_u2 + 2 * k2_u2 + 2 * k3_u2 + k4_u2)
        u3_val[i] = u3_val[i - 1] + (1 / 6) * (k1_u3 + 2 * k2_u3 + 2 * k3_u3 + k4_u3)

    return t, u1_val, u2_val, u3_val


def func_u1(t, u1, u2, u3):
    return u2 - u3 + t


def func_u2(t, u1, u2, u3):
    return 3 * t**2


def func_u3(t, u1, u2, u3):
    return u2 + exp(-t)


time, w1, w2, w3 = runge_kutta_system(
    func_u1, func_u2, func_u3, a=0, b=1, h=0.1, u10=1, u20=1, u30=-1
)

print(time)
print()
print(w1)
print()
print(w2)
print()
print(w3)
