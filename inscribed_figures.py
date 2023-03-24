import math
import sys

def areaOfcircle(length,radius):
    diagofreqcir = math.sqrt(2) * length-(2 * (math.sqrt(2) * radius))-(2 * radius)
    return math.pi * diagofreqcir / 2 * diagofreqcir / 2
   

def areaofsquare(length,radius):
    diagofreqsqr = math.sqrt(2) * length - (2 * (math.sqrt(2) * radius))-(2 * radius)
    return diagofreqsqr / math.sqrt(2) * diagofreqsqr / math.sqrt(2)

def inscribed_figures(length,radius,shape):
    if shape == 'CIR' and 2 * radius < length:
        return f"{areaOfcircle(length,radius):.2f}"
    elif shape == 'SQR' and 2 * radius < length:
        return f"{areaofsquare(length,radius):.2f}"
    else:
        return "please enter correct values"

print(inscribed_figures(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]))
