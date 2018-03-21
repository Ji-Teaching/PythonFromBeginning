from p03_4 import shuffled

def subsample(adData, iOne, iTwo):
    scrambled_list = shuffled(adData)
    adOne = scrambled_list[:iOne]
    adTwo = scrambled_list[-iTwo:]
    return [adOne, adTwo]
