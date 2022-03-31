import csv

# helper function to load csv data
def load_list_data(csv_file, column_name):

    lst = []

    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv file
        for row in csv_dict:
            # add the data from each row to a list
            if column_name in row:
                lst.append(row[column_name])
            else:
                print(f"{column_name} is undefined in this row")
                print(f"row: {row}")
            
        return lst