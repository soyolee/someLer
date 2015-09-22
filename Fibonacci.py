parents = (1)
babies = (1)
even = 0 
while babies < 4000000:
	print 'This generation has %s babies' %babies
	print 'This generation has {0} babies'.format(babies)
	parents, babies = (babies, parents + babies)
	if babies % 2 == 0:
		even += babies 
print even