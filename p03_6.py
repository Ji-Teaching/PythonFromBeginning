from p03_3 import testStatistic
from p03_5 import subsample

def nullDistribution( adData, iOne, iTwo ):
    adRet = []
    for i in range( 1000 ):
        adOne, adTwo = subsample( adData, iOne, iTwo )
        adRet.append( testStatistic( adOne, adTwo ) )
    return adRet
