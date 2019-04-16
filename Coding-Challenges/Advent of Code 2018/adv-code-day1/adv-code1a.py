def list_to_file(file):
	# Open a file in the main function, then append all of its value to a list
	# Then return the list as integers
	values = file.readlines()
	values = [e.strip() for e in values]
	# Parse all the elements to integers
	values = [int(e) for e in values]
	return values

def calc_total(num_list):
	# Take a list of numbers and return the sum
	total = 0
	for num in num_list:
		total += num
	return total

def main():
	# Work on the input.md file
	# f = open("input.txt", "r")
	f = open("input.md", "r")
	# A list of the frequencies
	freqs = list_to_file(f)
	# Print the total sum (i.e. resulting frequency)
	print(calc_total(freqs))
	f.close()

if __name__ == "__main__":
	main()