import peak

class TraceRecord(object):

    def __init__(self):
        self.sequence = []

    def getMaximum(self, arguments, maximun):
        """
               A function for recording the fact that the getMaximum function of
               some subproblem has been called.

               RUNTIME: O(1)
               """
        self.sequence.append({
            "type" : "findingMaximum" ,
            "coords" : arguments
        })

        self.sequence.append({
            "type" : "foundMaximum" ,
            "coord" : maximun
        })

    def getBetterNighbour(self, nighbour , better):
        """
              A function for recording the fact that the getBetterNeighbor function
              of some subproblem has been called.

              RUNTIME: O(1)
              """
        self.sequence.append({
            "type" : "findingNieghber" ,
            "coord" : nighbour
        })

        self.sequence.append({
            "type" : "foundNighber" ,
            "coor" : better
        })

