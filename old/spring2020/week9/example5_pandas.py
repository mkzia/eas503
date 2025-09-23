import numpy as np
import pandas as pd


employees = {
    'EmployeeID': ['EN1-26', 'EN1-33', 'EN1-35', 'EN1-36', 'EN1-38', 'EN1-40'],
    'Last_Name': ["O'Brien", "Guya", "Baranco", "Roslyn", "Schaaf", "Wing"],
    'First_Name': ["Sean", "Amy", "Steven", "Elizabeth", "Carol", "Alexandra" ]
}

df_employees = pd.DataFrame(employees)

projects = {
    'ProjectNum': [
        "30-452-T3", 
        "30-457-T3", 
        "30-482-TC", 
        "31-124-T3", 
        "31-238-TC",
        "31-238-TC2",
        "35-152-TC",
        "36-272-TC"
    ],
    'ProjectTitle': [
        "STAR manual",
        "ISO procedures",
        "Web site",
        "Employee handbook",
        "STAR prototype",
        "New catalog",
        "STAR pricing",
        "Order system"
    ]
}


df_projects = pd.DataFrame(projects)

print(df_projects)

employees_projects = {
    'EmployeeID': [
        "EN1-26", 
        "EN1-26", 
        "EN1-26", 
        "EN1-33", 
        "EN1-33", 
        "EN1-33", 
        "EN1-35", 
        "EN1-35", 
        "EN1-36", 
        "EN1-38", 
        "EN1-40", 
        "EN1-40",
    ],
    'ProjectNum' : [
        "30-452-T3",
        "30-457-T3",
        "31-124-T3",
        "30-328-TC",
        "30-452-T3",
        "32-244-T3",
        "30-452-T3",
        "31-238-TC",
        "35-152-TC",
        "36-272-TC",
        "31-238-TC2",
        "31-241-TC",
    ]


}

df_employees_projects = pd.DataFrame(employees_projects)

data = pd.merge(pd.merge(df_employees_projects, df_employees, how='left', on='EmployeeID'), df_projects,  how='left', on='ProjectNum')
print(data)