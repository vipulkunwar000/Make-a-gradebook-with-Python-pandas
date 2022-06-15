""" This file going to store the all info
related to the loading the data in the gradebook"""

from pathlib import Path
# Using the pathlib you can manipulate the paths in the system.
from pandas import pd

# keep track of the location
HERE = Path(__file__).parent
DATA_FOLDER = HERE/"data"

roster = pd.read_csv(
    DATA_FOLDER / "roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

# This line load the grade and homework file
hw_exam_grades = pd.read_csv(
    DATA_FOLDER / "hw_exam_grades.csv",
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID",
)

# This line of code will load the quizzes in the dataframe
# first empty data frame
# Loading the quizzess in the dat frame

quiz_grades = pd.DataFrame()
# This line finding the all the quizzes in the data file.
for file_path in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = " ".join(file_path.stem.title().split("_")[:2])
    quiz = pd.read_csv(
        file_path,
        converters={"Email": str.lower},
        index_col=["Email"],
        usecols=["Email", "Grade"],
    ).rename(columns={"Grade": quiz_name})
    # axis =1 showing that concatenation happening in the coloumns
    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)

# using converters we can convert the data into desired data
# type


# merge the data frame in the Python Pandas
# First I'll merge the roster and hw_examwork to get final data work
# Then this final data word merge to the quiz data file

# left index is True means that it treat left as a key.

final_data = pd.merge(roster,hw_exam_grades,left_index = True,right_index = True)


# let's merge the final data with the quiz_grades

final_data = pd.merge(final_data,quizz_grades,left_on = "Email Address", right_index = True)

# Here we've used the left_on to merge the email address on the left hand side of the dataframe
# Before calculating any value we need to check all the values
# If the value is Nan then need to replace with something


final_data = final_data.fillna(0)

n_exams = 3
for n in range(1, n_exams + 1):
    final_data[f"Exam {n} Score"] = (
        final_data[f"Exam {n}"] / final_data[f"Exam {n} - Max Points"]
    )
    
sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max

hw_max_renamed = homework_max_points.set_axis(homework_scores.columns, axis=1)

average_hw_scores = (homework_scores / hw_max_renamed).sum(axis=1)

# We need to get the average score
final_data["Average Homework"] = average_hw_scores/homework_scores.shape[1]

# We need homework score
# Here we've selected the two coloumns and find the maximum
# value from the two coloumns
final_data["Homework score"] = final_data[["Total Homework","Average Homework"].max(axis = 1)]


# Calculate the quiz score

# the quiz_Scores is used to the regex--- .filter to get the quizzes
quiz_scores = final_data.filter(regex=r"^Quiz \d$", axis=1)

# We're finding the maximum quiz points
# Getting the Series which will give the number of the coloumns
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
)

sum_of_quiz_scores = quiz_scores.sum(axis = 1)
# We need to find the maximum quiz scores
sum_of_quiz_max = quiz_max_points.sum()

# Lets figure out the total quizzes

final_data["Total quizzes"] = sum_of_quiz_scores/sum_of_quiz_max

# Let's figure out average quiz scores

average_quiz_scores = (quiz scores/quiz_max_points).sum(axis =1)

average_quiz_Scores = (quiz_score/quiz_max_points).sum(axis =1)

# This line finding the new column Average Quizzes
final_data["Average Quizzes"] = average_quiz_scores / quiz_scores.shape[1]

# We'll find the maximum quiz score which has highest value
final_data["Quiz Scores"] = final_data[["Total Quizzes","Average Quizzes"]].max(axis = 1)

# We need to calculate next the letter grade.

Weightings = pd.series(
    {
        "Exam 1 score":0.05,
        "Exam 2 score":0.1,
        "Exam 3 score":0.15,
        "Quiz Score":0.30,
        "Homework score":0.4,
        }
    )

# Combine the letter grades
final_data["Final Score"] = (final_data[weightings.index] * weightings).sum(
    axis=1
)
# np.ceil() gives the result in the round format
# This line logic is to come the line in the round format
final_data["Celling Score"] = np.ceil(final_data["Final Score"]*100
)

# Next we need to define the grades
# grades has assign in the form of the dictionary

grades = {
    90 : "A",
    80 : "B",
    70 : "C",
    60 : "D",
    0  : "F",
    }

# Next we're going to assign the grade letter with the help of the function
def grade_mapping(value):
    for key, letter in grades.item():
        if value >= key:
            return letter


# What's the logic of this line?
# 
letter_grades = final_data["Celling Score"].map(grade_mapping)


# Next we'll create the categorical coloumn
# What's the logic of the categorical data type?
# We've 5 choices to choose the correct choice we need to use categorical data type


final_data["Final Grade"] = pd.Categorical(
    letter_grades, categories=grades.values(), ordered=True
)

# What is a categories?
# Categories are the grade
# Why we've used the ordered data type
# It helps in building the sorted column in gradebook

# We need to put the data into the student adminstration

# Why we're groupping the data?

# We're grouping the data to associate each value to the letter grades

# We need to group the data by student section number and sort the results

# groupby() function is used to split the data into the groups by some criteria
for section, table in final_data.groupby("Section"):
    section_file = 

























