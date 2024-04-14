
def oneTimestep_FEuler(x, dt, f):
    return x + dt * f(x)


def oneTimestep_RK4(x, dt, f):
    k1 = f(x)
    k2 = f(x + dt / 2 * k1)
    k3 = f(x + dt / 2 * k2)
    k4 = f(x + dt / 2 * k3)
    return x + dt * (k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6)
