from p02_mean import mean
from p02_stdev import stdev

def testStatistic(adOne, adTwo):
    return (mean(adOne) - mean(adTwo)) / stdev(adOne + adTwo)
