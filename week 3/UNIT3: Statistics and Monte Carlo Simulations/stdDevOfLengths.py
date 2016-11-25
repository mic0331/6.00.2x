def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
    sizes = [len(s) for s in L]
    mean = sum(sizes)/len(L)
    var = (sum([(t - mean)**2 for t in sizes])/len(L))**.5
    return var

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

if __name__ == '__main__':
    L = [1, 2, 3]
    mean, std = getMeanAndStd(L)
    print("coefficient of variation", round(std/mean,3))