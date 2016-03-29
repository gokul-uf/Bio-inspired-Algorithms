import math
import random

# 1: Objective function f (x), x = (x 1 , . . . , x d ) T
# 2: Generate initial population of n host nests x i (i = 1, . . . , n)
# 3: while (t <MaxGeneration) or (stop criterion) do
# 4: Get a cuckoo randomly by L ́evy flights
# 5: Evaluate its quality/fitness F i
# 6: Choose a nest among n (say, j) randomly
# 7: if (F i > F j ) then
# 8: replace j by the new solution;
# 9: end if
# 10: A fraction (p a ) of worse nests are abandoned and new ones are built;
# 11: Keep the best solutions (or nests with quality solutions);
# 12: Rank the solutions and find the current best
# 13: end while

def compute_trip_length(trip):
	trip_length = distances[trip[0]][trip[-1]]
	for i in range(0,len(trip)-1):
		trip_length += distances[trip[i]][trip[i+1]]
	return trip_length

def create_random_nest(num_cities): 
	ret_val = range(num_cities)
	random.shuffle(ret_val)
	return ret_val

def create_nest(num_cities, ): #TODO
	pass

def generate_cuckoo(num_cities, ): #TODO
	pass

def prune_nests(nests,pa):
	# dict_of_nests = {}
	# for nest in nests:
	# 	trip_length = compute_trip_length(nest)
	# 	if trip_length in dict_of_nests:
	# 		dict_of_nests[trip_length].append(nest)
	# 	else:
	# 		dict_of_nests[compute_trip_length(nest)] = [nest]
	# sorted_nest_indices = sorted(dict_of_nests)
	# sorted_nests = [dict_of_nests[i] for i in sorted_nest_indices]
	# return sorted_nests[:-pa]
	sorted_nests = sorted(nests, key=compute_trip_length)
	return sorted_nests[:-pa]

if __name__ == "__main__": 
	distances = [[]] #INPUT, input distance matrix
	num_nests = 1 #INPUT, total number of nests. Same as the number of birds
	num_cities = 1 #INPUT, total number of cities
	num_iterations = 1 #INPUT, number of iterations the main loop should run
	pa = 0.02*num_nests #INPUT, fraction of nests to be discarded after each iteration
	nests = []
	i = 0
	while (i<num_nests):
		nest = create_nest(num_cities)
		if nest not in nests:
			nests.append(nest)
			i+=1
	print "Nests created"
	for i in range(num_iterations):
		cuckoo = generate_cuckoo(num_cities, )
		random_nest = random.randint(0,num_nests-1)
		if compute_trip_length(cuckoo) <= compute_trip_length(nests[random_nest]):
			nests[random_nest] = cuckoo
		nests = prune_nests(nests,pa)
		print "Iteration Number: {}".format(i+1)
		print "Best result: {}".format(nests[0])
		print "Trip length: {}".format(compute_trip_length(nests[0]))
		for i in range(pa):
			nest = create_nest(num_cities)
			nests.append(nest)
		
