import sys
import peak
import utils


def loadProblem(file = "problems.py" , variable = "problemMatrix"):
    """
       Loads a matrix from a python file, and constructs a PeakProblem from it.
    """

    namespace = dict()
    with open(file) as handler :
        exec (handler.readline(), namespace)
    return peak.createProblem(namespace[variable])


def main():
    if len(sys.argv) > 1 :
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFileName("problem.py"))

    # run all algorithims , gathering the trace and priniting out results as we go

if __name__ == "__main__" :
    main()