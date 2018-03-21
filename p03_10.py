def readPCL( fileIn ):
	astrConditions = []
	astrGenes = []
	astrNames = []
	aadData = []
	for line in fileIn:
		astrLine = line.split('\t')
		if not astrConditions == []:
			astrGenes.append(astrLine[0])
			astrNames.append(astrLine[1])
			adData = []
			for data_str in astrLine[2:]:
				data_float = float(data_str)
				adData.append(data_float)
			aadData.append(adData)
		else:
			astrConditions = astrLine[2:]
	return [astrConditions, astrGenes, astrNames, aadData]

if __name__ == "__main__":
	astrConditions, astrGenes, astrNames, aadData = readPCL( open( "dilution_rate_02_knn.txt" )  )
# You could also use	readPCL( open( "dilution_rate_02_knn.txt" ) )
# Or you could use	readPCL( open( sys.argv[1] ) )
	print( "\t".join( astrConditions ) )
	print( "\t".join( astrGenes ) )
	print( "\t".join( astrNames ) )
	for adData in aadData:
		astrData = []
		for dDatum in adData:
			astrData.append( str(dDatum) )
		print( "\t".join( astrData ) )
