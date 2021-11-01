import pandas
import numpy

#Function to import csv file
def import_csv(filepath):
#Reading and saving csv to a variable
    csv_file = pandas.read_csv(filepath)
    return csv_file
#Function to look for Average and replace missing values- Horsepower
def average_replace_missing_value(csv_file):
    csv_file['horsepower']=csv_file['horsepower'].fillna(csv_file['horsepower'].mean())
#Function to look for minimum and replace missing value-Origin values
def minimum_replace_missing_value(csv_file):
    csv_file['origin']=csv_file['origin'].fillna(csv_file['origin'].min())
#Funtion to generate data file
def generate_data_file(csv_file, csv_file_2):
    csv_file.to_csv("output/question1 out.csv", index=False, columns=csv_file.columns)
    csv_file_2.to_csv("output/question2 out.csv", index=False, columns=csv_file_2.columns)
#Function to rename -name to car name
def rename_name_to_car_name(csv_file):
    csv_file.rename(columns={"name":"car name"})
#Function to add new column Others
def add_other_column(csv_file):
    csv_file.insert(len(csv_file.columns), 'other', [1 for x in csv_file['acceleration']])
    

#This solves the question 4 and 5
def main():
    csv_file = import_csv('specs\AutoMpg_question1.csv')
    average_replace_missing_value(csv_file)
    minimum_replace_missing_value(csv_file)

    new_file = import_csv('specs\AutoMpg_question2_a.csv')
    new_file_two = import_csv('specs\AutoMpg_question2_b.csv')
    rename_name_to_car_name(new_file_two)
    add_other_column(new_file)
   



    csv_file_2 = pandas.concat([new_file, new_file_two])
    generate_data_file(csv_file, csv_file_2)



if __name__=="__main__":
    main()


