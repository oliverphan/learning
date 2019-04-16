def file_to_list(file):
	# Open a file in the main function, then append all of its value to a list
	# Then return the list as integers
	values = file.readlines()
	values = [e.strip() for e in values]
	# Parse all the elements to integers
	values = [int(e) for e in values]
	return values

def first_repeated(num_list, starting, seq_list):
	"""Find the first repeated sum in num_list"""

	if (starting + num_list[0]) in seq_list:
		return starting
	else:
		beg = starting
		seq_list.append(beg)
		for num in num_list:
			beg += num
			if beg in seq_list:
				return beg
			else:
				seq_list.append(beg)
		return first_repeated(num_list, beg, seq_list)


def main():
	# Work on the input.md file to return the first repeated frequency
	f = open("input.md", "r")
	# A list of the frequencies
	changes = file_to_list(f)
	print(len(changes))
	begin_dict = {0: 0}
	repeated = first_repeated(changes, 0, [0])
	print(repeated)
	f.close()

if __name__ == "__main__":
	main()