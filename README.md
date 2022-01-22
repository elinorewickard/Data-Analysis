# Overview
The data set I am using is from kaggle, it contains the top 200 passwords from 49 countries. It has the columns:
 country_code,country,Rank,Password,User_count,Time_to_crack,Global_rank,Time_to_crack_in_seconds.
It can be found [here](https://www.kaggle.com/prasertk/top-200-passwords-by-country-2021)

This software was a venture in using pandas for data analysis. It was created as a learning experience and is not perfect.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results
1. What is the top global password? How fast is it to crack it?
    - The global password is: 123456.
    It took 0 seconds to crack.
2. Which password took the longest to crack in your country?
    - This one allows the user to select a country and it shows which password took the longest and the time it took to crack.
3. What password has the lowest user count in your country?
    - This also allows the user to select a country to view which password has the fewest users among the top 200 passwords.

# Development Environment

- VS Code
- Python 3.8.6 64-bit
- Pandas library
- Data set from Kaggle, top_200_password_2020_by_country.csv

# Useful Websites

* [kaggle](https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas)
* [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)

# Future Work

* Improve how some of the data is presented
* Increase question bank
