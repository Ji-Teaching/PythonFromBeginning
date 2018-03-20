def ptoq( adX ):

	adY = sorted( adX )
	for i in range( len( adY ) ):
		adY[i] = adY[i] * len( adY ) / ( i + 1.0 )
	return adY
