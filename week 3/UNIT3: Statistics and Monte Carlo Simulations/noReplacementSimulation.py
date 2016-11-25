import random
import numpy as np

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    bucket = ["R"]*3 + ["G"]*3
    same_color = 0
    for trial in range(numTrials):
        hand = np.random.choice(bucket, 3, replace=False)
        #random.shuffle(bucket)
        #hand = [bucket[x] for x in range(3)]
        same_color += 1 if all(x == hand[0] for x in hand) else 0
    return round(same_color/numTrials, 3)

def noReplacementSimulation1(numTrials):
    bucket = np.array([True, True, True, False, False, False], bool)
    same_color = 0
    for trial in range(numTrials):
        np.random.shuffle(bucket)
        same_color += 1 if all(bucket[:3]) else 0
    return round(2 * same_color / numTrials, 3)

if __name__ == '__main__':
    print(noReplacementSimulation(5000))
