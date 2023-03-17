import aocd
from time import perf_counter


def run_solver(day, level, solver, input):
    start_time = perf_counter()
    answer = solver(input)
    elapsed_time = perf_counter() - start_time
    print(f"Day {day}, Part {level}: {answer:<30} ({elapsed_time:.4f}s)")


def solve(day, parse, *solvers):
    data = aocd.get_data(day=day, year=2022)
    for i, solver in enumerate(solvers):
        run_solver(day, i+1, solver, parse(data))
