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

# takes the function load_list_data and loads each column into 
# an empty variable

ages = load_list_data('insurance.csv', 'age')
sexes = load_list_data('insurance.csv', 'sex')
bmis = load_list_data('insurance.csv', 'bmi')
children = load_list_data('insurance.csv', 'children')
smokers = load_list_data('insurance.csv', 'smoker')
patient_region = load_list_data('insurance.csv', 'region')
patient_insurance_charges = load_list_data('insurance.csv', 'charges')

# this function loops through the array and adds each unique region 
# into a new array, as long as it is not already in the array

def different_regions(l):
    unique_regions = []

    for region in patient_region:
        if region not in unique_regions:
            unique_regions.append(region)
    return unique_regions