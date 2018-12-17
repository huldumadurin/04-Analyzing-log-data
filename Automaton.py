import re

class Automaton:
    def __init__(self):
        self.alphabet = "ABCD"
        self.nextStates = {'': ['A'], 'A': ['B', 'C'], 'B': ['C', 'B'], 'C': ['B', 'D'], 'D': []}
        self.acceptStates = ['D']
        self.instances = []
        self.done = []
        self.stuck = []

    def monitorInstances(self):
        for i in self.instances:
                oldState = i.currentState
                i.doNextLine()
                
                if i.currentState == oldState and oldState not in self.nextStates[oldState]:
                    print(i.filename + " is stuck on state " + oldState + ". ", end='')
                    if i.currentState in self.acceptStates:
                        print("However, this is an accepting state.", end='')
                        self.done.append(i)
                    else:
                        self.stuck.append(i)
                    print("")
                elif i.currentState not in self.nextStates[oldState] or i.currentState not in self.alphabet:
                    i.badTransitions.append(str("Bad transition in " + i.filename + " at line " + str(i.linecount) + ". [" + oldState + " -> " + str(i.currentState) + "]"))
                
                

        for i in self.done:
            if i in self.instances:
                self.instances.remove(i)
        for i in self.stuck:
            if i in self.instances:
                self.instances.remove(i)
        

class Instance():
    def __init__(self, filename):
        self.filename = filename
        self.currentState = ''
        self.linecount = 0
        self.regex = re.compile("action: ([A-Z]);")
        self.badTransitions = []

    def doNextLine(self):
        with open(self.filename) as file:
            for i, line in enumerate(file):
                if(i == self.linecount):
                    self.currentState = self.getAction(line)
                    self.linecount = self.linecount + 1
                    return
    
    def getAction(self, line):
        m = re.search("action: ([A-Z]);",line)
        if m:
            nextAction = m.group(1)
        else:
            nextAction = self.currentState
        return nextAction
    
    def printBad(self):
        for t in self.badTransitions:
            print("\t\t" + t)
    
    def printState(self):
        print("state " + str(self.currentState) + ", line " + str(self.linecount))



a = Automaton()

a.instances.append(Instance("23.log"))
a.instances.append(Instance("24.log"))
a.instances.append(Instance("25.log"))


while len(a.instances) > 0:
    a.monitorInstances()

print("Finished:")
for i in a.done:
    print("\t " + i.filename + " finished with ", end='')
    i.printState()
    i.printBad()

print("Stuck:")
for i in a.stuck:
    print("\t " + i.filename + " stuck at ", end='')
    i.printState()
    i.printBad()
