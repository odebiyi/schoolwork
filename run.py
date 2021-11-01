from sqlalchemy import create_engine
import pandas
from sqlalchemy import engine
import matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


from sqlalchemy.engine import result

#function to import csv
def import_csv(filepath):
    dataset_csv = pandas.read_csv(filepath)
    return dataset_csv
    

def question2_4():
    df = import_csv('./specs/DW_Dataset.csv')
   
    threedee = plt.figure().gca(projection='3d')
    
    df[" Status"].replace({"Director": 0, "Technician": 1, "Senior Technician":2, "Deputy Director":3}, inplace=True)
    threedee.scatter(df['Year of Birth'], df[' Salary'], df[' Status'])
    threedee.set_xlabel('Year of Birth')
    threedee.set_ylabel('Salary')
    threedee.set_zlabel('Status')
    plt.show()




def main():

    question2_4()


    db_string = "postgresql://postgres@localhost:5432/question3"

    engine = create_engine(db_string)
    engine.execute("CREATE TABLE IF NOT EXISTS big_university (student_key integer, instructor_key integer, course_key varchar,semester_key char, count integer, avg_grade char )")
    dataset_csv=import_csv('./specs/input_DW_data.csv')

def read_record (field, name, engine):
    result = engine.execute("SELECT * from big_university where "+field +"="+ name)
    return result
def write_record (name, details, engine):
    engine.execute("INSERT INTO big_university "+ name +" VALUES "+details)
def update_record (field_name, new_value, engine):
    engine.execute(f"UPDATE big_university SET {field_name}={new_value}")
def read_dataset (name, engine):
    result = engine.execute(f"SELECT {name} from big_university")
    return result;
def write_dataset (name, dataset, engine):
    engine.execute("INSERT INTO big_university "+ name +" VALUES "+dataset)
    
def list_datasets (engine):
    result = engine.execute("SELECT * from big_university")
    for i in result:
        print(i)
if __name__ == '__main__':
    main()