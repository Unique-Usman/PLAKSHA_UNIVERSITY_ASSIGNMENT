import pandas as pd
import numpy as np

def studentinfo(filename):
    #checking if the file is present
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    #ensure file contains at least one row
    df = pd.read_csv(filename)

    if df.empty:
        raise Exception("File is empty")

    # Ensure that column names match the ones in the CSV file
    df.columns = [col.strip() for col in df.columns]

    df["Name"] = df["Name"].str.strip()
    df["City"] = df["City"].str.strip()

    #getting the highest visited city and highest occurence name
    most_visited_city = df["City"].mode()[0]
    highest_name = df["Name"].mode()[0]

    #replacing the city and the name which are null to the highest
    #occuring one
    df["City"].fillna(most_visited_city, inplace=True)
    df["Name"].fillna(highest_name, inplace=True)

    #calculating the average age
    average_age = df["Age"].mean
    df["Age"].fillna(average_age, inplace=True)

    average_age_by_city = df.groupby('City')['Age'].mean().to_dict()
    return average_age_by_city

def dssalary(filename, expected_salary):
    #checking if the file is present
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    #ensure file contains at least one row
    df = pd.read_csv(filename)

    if df.empty:
        raise Exception("File is empty")
    #dropping the column
    df.dropna(inplace=True)

    # Ensure that column names match the ones in the CSV file
    df.columns = [col.strip() for col in df.columns]

    df['employment_type'] = df['employment_type'].str.strip()
    df['job_title'] = df['job_title'].str.strip()
    df['employee_residence'] = df['employee_residence'].str.strip()
    df['company_size'] = df['company_size'].str.strip()

    readData = df[ (df['employment_type'] == "FT") & (df['job_title'] == "Data Scientist") &
            ((df['employee_residence'] == "CA") | (df['employee_residence'] == "US")) & (df['company_size'] == "L") ]

    avg_salary = readData['salary_in_usd'].mean()

    if avg_salary >= expected_salary:
        return "satisfied"
    else:
        return "unsatisfied"

def increment(filename, salary_raise):

    #checking if the file is present
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    #ensure file contains at least one row
    df = pd.read_csv(filename)

    if df.empty:
        raise Exception("File is empty")

    for job_title, perecent_increment in salary_raise.items():
        job_title = job_title.strip()

    if job_title in df['job_title'].values:
        incrementAmt = (perecent_increment / 100) * df.loc[df['job_title'] == job_title, 'salary'].values[0]

        df.loc[df['job_title'] == job_title, 'salary'] += incrementAmt
        df.loc[df['job_title'] == job_title, 'salary_in_usd'] += incrementAmt

    df.to_csv(filename, index = False)

    return df

def preprocess(filename):


    #checking if the file is present
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError()

    #ensure file contains at least one row
    df = pd.read_csv(filename)

    if df.empty:
        raise Exception("File is empty")

    df['work_year'] = pd.to_datetime(df['work_year'], format = '%Y')

    startDate = pd.to_datetime('2020-01-01', format = '%Y-%m-%d')
    endDate = pd.to_datetime('2021-01-01', format = '%Y-%m-%d')
    df = df[(df['work_year'] >= startDate) & (df['work_year'] <= endDate)]

    df = df.drop(columns = ['remote_ratio', 'experience_level'])

    return df


def jobsearch(filename1, filename2):
    #checking if the file is present
    try:
        df_buddies = pd.read_csv(filename1)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    #ensure file contains at least one row
    df_buddies = pd.read_csv(filename1)

    if df_buddies.empty:
        raise Exception("File is empty")

    #checking if the file is present
    try:
        df_salaries = pd.read_csv(filename2)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    #ensure file contains at least one row
    df_salaries = pd.read_csv(filename2)

    if df_salaries.empty:
        raise Exception("File is empty")

    mergedData = pd.merge(df_buddies, df_salaries, on = ['job_profile', 'location'], how = 'inner')

    return mergedData


if __name__ == "__main__":
    pass
