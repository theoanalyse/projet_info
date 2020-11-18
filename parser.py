from coordinate import Coordinate

def parse_csv(csv_file):
	coordinates = []

	with open(csv_file) as fp:
		next(fp) # used to ignore the header
		for line in fp:	
			tokens = line.strip().split(',')
			coordinates.append(Coordinate(float(tokens[2]), float(tokens[3]), tokens[1]))
    	
	return coordinates
    	
def parse_adjacency_matrix(matrix_file):
	adjacency_matrix = []
	with open(matrix_file) as fp:
		for line in fp:
			tokens = [float(x) for x in line.strip().split(' ')] # transform the line in a list
			adjacency_matrix.append(tokens)
	return adjacency_matrix
