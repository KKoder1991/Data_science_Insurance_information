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


# this function calculates the average age of the users in the data set
def sum_of_list(l):
    total = 0
    for val in l:
        total = total + int(val)
    return total

# this function is to see how many males or how many females are in 
# the dataset given

def number_of_occurences(l, property):
    count = 0 
    for value in l:

        if value == property:
            count += 1
    return count

# this function loops through the array and adds each unique region 
# into a new array, as long as it is not already in the array

def different_regions(l):
    unique_regions = []

    for region in patient_region:
        if region not in unique_regions:
            unique_regions.append(region)
    return unique_regions

#This section containts the information that was needed to be extracted
# from the given data. Each answer is saved to a variable

#This is for the average age of the people insured in the dataset
average_age = round(sum_of_list(ages) / len(ages))
print(average_age)
#This is for the amount of males inside the dataset
males_in_dataset = number_of_occurences(sexes, 'male')
print(males_in_dataset)
#Total number of people insured
total_number_of_insured = len(ages)
number_of_smokers = count_number_occurences(smokers, "yes")
unique_regions = different_regions(patient_regions)


