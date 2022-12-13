# change the following scores and run the script
participation_percent = 70 / 100
prelim1_percent = 88 / 100
prelim2_percent = 93.9 / 100
final_percent = 68.5 / 100
homework_percent = 96.15 / 100
homework_challenge = 40 / 100

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")

participation = solver.NumVar(0, solver.infinity(), "participation")
prelim1 = solver.NumVar(0, solver.infinity(), "prelim1")
prelim2 = solver.NumVar(0, solver.infinity(), "prelim2")
final = solver.NumVar(0, solver.infinity(), "final")
homework = solver.NumVar(0, solver.infinity(), "homework")
homeworkchl = solver.NumVar(0, solver.infinity(), "homeworkchl")


solver.Add(participation + prelim1 + prelim2 + homework + final <= 100.0)
solver.Add(participation + prelim1 + prelim2 + homework + final >= 100.0)

solver.Add(participation >= 0)
solver.Add(participation <= 3)

solver.Add(prelim1 >= 10)
solver.Add(prelim1 <= 25)

solver.Add(prelim2 >= 10)
solver.Add(prelim2 <= 25)

solver.Add(homework >= 30)
solver.Add(homework <= 30)

solver.Add(homeworkchl <= 2.5)
solver.Add(homeworkchl >= 2.5)

solver.Add(final >= 25)
solver.Add(final <= 40)

solver.Maximize(
    participation_percent * participation
    + prelim1_percent * prelim1
    + prelim2_percent * prelim2
    + homework_percent * homework
    + homework_challenge * homeworkchl
    + final_percent * final
)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Final Score (Pratyush):", solver.Objective().Value(), "🙌")
else:
    print("make sure your scores are valid and try again!")
