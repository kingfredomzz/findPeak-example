import peak
import trace

def algorthim1 (problem , trace = None):
    # if it's empty, we are done
    if problem.numRow <= 0 or problem.numCol <= 0 :
        return None
    # the recursive subproblem will involve half the number of columns
    mid = problem.numCol // 2

