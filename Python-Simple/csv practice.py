import csv


def create_rate_groups(WSIB_CSV_file):
    """
    Takes the CSV file with the rate groups and makes the dictionary for the
    rates with rate group.

    Key (str): rg###
    Value (float): #####
    """
    rate_groups = {}
    with open(WSIB_CSV_file) as file:
        for line in csv.reader(file):
            name= 'rg' + str(line[0])
            rate_groups[name] = float(line[2])
    return rate_groups
