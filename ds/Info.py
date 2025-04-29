
class Info:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def toString(self):
        return "start: " + str(self.start) + " end: " + str(self.end)