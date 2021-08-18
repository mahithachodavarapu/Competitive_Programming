# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.




def fun_nearestbusstop(street):
	dec=(street/8)-(street//8)
	if(dec>0.5):
		return ((street//8)+1)*8
	return (street//8)*8
