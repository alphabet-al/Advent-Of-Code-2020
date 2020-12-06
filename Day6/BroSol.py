def criteria_one( data ):
	answers = [ ]
	total_answers = [ ]
	yes_answers = 0

	for _, line in enumerate( data ):
		if line != '':
			answers = answers + list( line )

		if line == '' or line == data[ -1 ]:
			unique_answers = sorted( set( answers ) )
			total_answers.append( unique_answers )
			answers = [ ]

	for idx, answer_group in enumerate( total_answers ):
		yes_answers += len( answer_group )
		# print( '\tNumber of "YES" answers in this group: {0}'.format( len( answer_group ) ) )

	return yes_answers


def criteria_two( data ):
	answers = [ ]
	total_answers = [ ]
	yes_answers = 0

	for idx, line in enumerate( data ):
		
		if line != '':
			answers.append( set( list( line ) ) )
			

		if line == '' or idx == len( data ) - 1:
			shared_answers = set.intersection( *answers )
			print(shared_answers)
			total_answers.append( len( shared_answers ) )
			answers = [ ]

	for idx, answer_group in enumerate( total_answers ):
		yes_answers += answer_group
		# print( '\tNumber of "YES" answers in this group: {0}'.format( answer_group ) )

	return yes_answers



if __name__ == "__main__":
	input = r'C:\Users\alanv\PythonCode\Projects\Advent of Code 2020\Day6\custom_data.txt'
	data = [ ]
	yes_answers = 0

	with open( input, 'r' ) as input_file:
		data = [ line.strip( ) for line in input_file.readlines( ) ]

	yes_answers = criteria_one( data )
	shared_answers = criteria_two( data )

	# print( '\nNumber of questions answered "YES" to: {0}'.format( yes_answers ) )
	# print( '\nNumber of questions all answered "YES" to: {0}'.format( shared_answers ) )