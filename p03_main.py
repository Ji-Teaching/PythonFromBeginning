from p03_2 import listStartsWith
from p03_3 import testStatistic
from p03_6 import nullDistribution
from p03_7 import listSlice
from p03_8 import pvalue
from p03_9 import oneToTwoTailed
from p03_10 import readPCL

def testSomeGenes( fileIn, astrTargetsGene, astrTargetsOne, astrTargetsTwo ):
    astrConditions, astrIDs, astrNames, aadData = readPCL( fileIn )
    aiGenes = listStartsWith( astrIDs, astrTargetsGene )
    aiOne = listStartsWith( astrConditions, astrTargetsOne )
    aiTwo = listStartsWith( astrConditions, astrTargetsTwo )
    aastrRet = []
    for iGene in aiGenes:
        adData = aadData[iGene]
        adNull = nullDistribution( adData, len( aiOne ), len( aiTwo ) )
        dP = oneToTwoTailed( pvalue( testStatistic( listSlice( adData, aiOne ),
            listSlice( adData, aiTwo ) ), adNull ) )
        if dP < 0.01:
            aastrRet.append( [astrIDs[iGene], astrNames[iGene], str(dP)] )
    return aastrRet

if __name__ == "__main__":
# Genes from chromosome X differential between phosphate and nitrate
    aastrGenes = testSomeGenes( open( "dilution_rate_02_knn.txt" ) , ["YJ"], ["P"], ["N"] )
    for astrGene in aastrGenes:
        print( "\t".join( astrGene ) )
