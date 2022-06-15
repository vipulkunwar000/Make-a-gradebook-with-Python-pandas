 #groupby() function is used to split the data into the groups by some criteria
for section, table in final_data.groupby("Section"):
    # Next we need to show the section file in the data folder
    section_file = DATA_FOLDER/f"Section {section} Grades.csv"
    
    num_students = table.shape[0]
    
    print(f"In section {section} there are {num_students} students saved to "
          f"file {section_file}")
    
    # to_csv() file is used to give the value to the CSV file
    
    # Next we need to sort the value by sort_values function
    
    table.sort_values(by=["Last name","First name"]).to_csv(section_file)
    

    

    
    
    
