def degreesToSteps(degrees):
    stepsPerDegree = float(4096 / float(360)) 
    return float(stepsPerDegree * degrees)
