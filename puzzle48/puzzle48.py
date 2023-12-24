from z3 import *


# Got this idea from github copilot. Don't know how the z3-solver works.
def solve_special_point(points):
    # Define Z3 variables for the special point's position and velocity
    x, y, z = Reals("x y z")
    vx, vy, vz = Reals("vx vy vz")

    # Initialize the Z3 solver
    solver = Solver()

    # Create a variable for time for each point
    time_vars = [Real(f"t_{i}") for i in range(len(points))]

    # For each point and corresponding time variable, create equations
    for i, point in enumerate(points):
        X, Y, Z, Vx, Vy, Vz = point
        t = time_vars[i]

        # Equations for each point
        solver.add(x + t * vx == X + t * Vx)
        solver.add(y + t * vy == Y + t * Vy)
        solver.add(z + t * vz == Z + t * Vz)

        # Ensure time is positive for intersection
        solver.add(t > 0)

    # Check if the system has a solution
    if solver.check() == sat:
        # Get the model if a solution exists
        model = solver.model()
        x, y, z = model.eval(x), model.eval(y), model.eval(z)
        x, y, z = x.as_long(), y.as_long(), z.as_long()
        return x, y, z


def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    inputs = []
    for line in lines:
        p, v = line.split(" @ ")
        p = list(map(int, p.split(",")))
        v = list(map(int, v.split(",")))
        inputs.append([*p, *v])

    return sum(solve_special_point(inputs))


print(solution("input.txt"))
