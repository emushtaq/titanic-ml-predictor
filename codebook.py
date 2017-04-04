import pandas

# We can use the pandas library in Python to read in the CSV file
# This creates a pandas dataframe and assigns it to the titanic variable
titanic = pandas.read_csv("train.csv")

# Print the first five rows of the dataframe
print(titanic.head(5))