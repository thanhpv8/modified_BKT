import matplotlib.pyplot as plt 


def readTrainPredict(train):
    skill = []
    fh = open('convergence.txt')
    while True:
        # read line
        line = fh.readline()
        if not line:
            if(hasData):
                plotGraph(title, "Iteration", "LogLikelihood", x, y)
            hasData = False
            break
        if line.startswith('skill'):
            if(hasData):
                plotGraph(title, "Iteration", "LogLikelihood", x, y)
            hasData = True
            title =""
            x=[]
            y=[]

            line1 = line.strip().split(':')
            title = line1[1]
            column_header = fh.readline()
        else:
            line1 = line.strip().split('\t')
            x.append(int(line1[0]))
            y.append(float(line1[1]))
       
    fh.close()

def graphConvergence():
    title =""
    x=[]
    y=[]
    hasData = False
    fh = open('convergence.txt')
    while True:
        # read line
        line = fh.readline()
        if not line:
            if(hasData):
                plotGraph(title, "Iteration", "LogLikelihood", x, y)
            hasData = False
            break
        if line.startswith('skill'):
            if(hasData):
                plotGraph(title, "Iteration", "LogLikelihood", x, y)
            hasData = True
            title =""
            x=[]
            y=[]

            line1 = line.strip().split(':')
            title = line1[1]
            column_header = fh.readline()
        else:
            line1 = line.strip().split('\t')
            x.append(int(line1[0]))
            y.append(float(line1[1]))
       
    fh.close()

def graphMastery():
    title =""
    x=[]
    y=[]
    hasData = False
    fh = open('mastery.txt')
    while True:
        # read line
        line = fh.readline()
        if not line:
            if(hasData):
                plotGraph(title, "Opportunity", "Mastery", x, y)
            hasData = False
            break
        if line.startswith('skill'):
            if(hasData):
                plotGraph(title, "Opportunity", "Mastery", x, y)
            hasData = True
            title =""
            x=[]
            y=[]

            line1 = line.strip().split(':')
            title = line1[1]
            column_header = fh.readline()
        else:
            line1 = line.strip().split('\t')
            x.append(int(line1[0]))
            y.append(float(line1[1]))
       
    fh.close()

def plotGraph(title, xlabel, ylabel, x, y):
    figure = plt.figure()
    plt.grid(True)
    # plotting the points  
    plt.plot(x, y) 
    
    # naming the x axis 
    plt.xlabel('x - '+xlabel) 
    # naming the y axis 
    plt.ylabel('y - '+ylabel) 
    
    # giving a title to my graph 
    plt.title(title) 

# =========================================== #
graphConvergence()
graphMastery()
plt.show()