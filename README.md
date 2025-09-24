# Programming Assignment #3
This file contains the codes for Programming Assignment #1, which includes the following problems:

Problem 1. Save your file as Surname_Pandas-P1.py
   - Load the corresponding .csv file into a data frame named cars using pandas
   - Display the first five and last five rows of the resulting cars

Problem 2. Save your file as Surname_Pandas-P2.py
  - Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
  - Display the row that contains the ‘Model’ of ‘Mazda RX4’.
  - How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
  - Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
  Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library

# CODE AND EXPLANATION

## Problem 1

    ### Code: 
    import pandas as pd
    cars = pd.read_csv('cars.csv')
    cars
    cars.head()
    cars.tail()

## EXPLANATION

  import pandas as pd 
  - Imports the Pandas Library

  cars = pd.read_csv('cars.csv')
  cars
  - Loads the dataset (cars) from the file cars.csv.

  cars.head()
  - Shows the first 5 rows.

  cars.tail()
  - Shows the last 5 rows.
    
## Problem 2

    ### Code:
    cars.loc[0:4,::2]
    cars.loc[(cars['Model'] == 'Mazda RX4')]
    cars.loc[(cars['Model'] == 'Camaro Z28', ['cyl'])]
    cars.loc[(cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['cyl', 'gear'])]

## EXPLANATION

a. First 5 Rows with Odd-Numbered COlumns
  cars.loc[0:4,::2]
  - Selects rows 0 to 4 (the first 5 rows)
  - ::2 is intended to select every 2nd column (odd-numbered columns)

b. Row for Mazda RX4
   cars.loc[(cars['Model'] == 'Mazda RX4')]
   - Looks for rows where the Model column -"Mazda RX4"
   - Prints the full row of Mazda RX4

c. Cyclinders for Camazro Z28
    cars.loc[(cars['Model'] == 'Camaro Z28', ['cyl'])]
    - Looks for rows where the Model column -"cAMARO Z28"
    - Returns only the cyl column

d. Cylinders and Gear of Specific Models
    cars.loc[(cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), 
    ['cyl','gear'])]
    - .isin([]) checks if the Model is one of the listed cars.
    - Prints only the cyl and gear columns for those models.

## SUMMARY
- Loaded cars.csv into a Pandas DataFrame.
- Displayed the first and last 5 rows.
- Extracted specific rows and columns using slicing and filtering.
- First 5 rows with odd columns
- Details of Mazda RX4
- Cylinders of Camaro Z28
- Cylinders + gears of Mazda RX4 Wag, Ford Pantera L, and Honda Civic.

