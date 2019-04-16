def file_to_list(filename):
	values = filename.readlines()
	values = [v.strip() for v in values]
	# List of strings
	return values

def count_repeats(string_list):
	"""Return the number of double repeated letters * triple repeated letters"""
	
	pairs = 0
	triplets = 0
	# Easy case: String has exactly one pair
	# Medium Case: String has exactly one triplet
	# Hard case: String has dual pair/triplet
	# Hard Case: String has a pair and a triplet

	return pairs * triplets


def main():
	f = open("input.md", "r")
	boxIDs = file_to_list(f)
	print(count_repeats(boxIDs))
	f.close()

if __name__ == "__main__":
	main()