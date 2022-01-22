"""
Data Analysis Software with pandas in python
Elinore Wright
"""
import pandas as pd

def printOptions():
    '''Just prints out the available questions for user to choose.'''
    
    print()
    print("1. What is the top global password? How fast is it to crack it?")
    print("2. Which password took the longest to crack in a country?")
    print("3. What password has the lowest user count in a country?") 
    print("4. What were the top 10 passwords for a country?")
    print("q. Quit")
    print()

def answerOne(df):
    '''Answer: What is the top global password? How fast is it to crack it?'''

    #grab global rank password and time it took to crack
    password = df.loc[df["Global_rank"] == 1, "Password"]
    time = df.loc[df["Global_rank"] == 1, "Time_to_crack_in_seconds"]
    print(f"The global password is: {password[0]}.")
    print(f"It took {time[0]} seconds to crack.")
    
def answerTwo(df, dict):
    '''Answer: Which password took the longest to crack in a country?
    Dictionary is passed through to check input against.'''

    #get input form user and check against the list to see if it is viable
    country = str(input("What is your two letter country code? ")).lower()
    if country in dict:
        #grabs the highest time for the selected country
        time = df.loc[df["country_code"] == country, "Time_to_crack_in_seconds"].max()

        #grabs the corresponding password with the highest time
        password = df.loc[(df["country_code"] == country) & (df["Time_to_crack_in_seconds"] == time), "Password"]

        #password is being displayed funny, password[0] doesn't work for some reason
        print(f'The password was:\n{password.to_string()}.')
        print(f'For the country {dict[country]}, it took {time} seconds to crack.')

    else:
        print(f'{country} is not a country code available in this data.')
    
def answerThree(df, dict):
    '''Answer: What password has the lowest user count in a country?
    Dictionary is passed through to check input against'''
    
    country = str(input("What is your two letter country code? ")).lower()
    if country in dict:
        #grabs the lowest user_count for selected country
        counts = df.loc[df["country_code"] == country, "User_count"].min()

        #grabs the corresponding password with the lowest user_count
        password = df.loc[(df["country_code"] == country) & (df["User_count"] == counts), "Password"]
        #password display fixed!
        print(f'The least used password was\n{password.to_string()}\n for country {dict[country]} with {counts} many users.')

    else:
        print(f'{country} is not a country code available in this data.')

def answerFour(df, dict):
    '''Answer: What were the top 10 passwords for a country?
    Dictionary is passed through to check input against'''

    country = str(input("What is your two letter country code? ")).lower()
    if country in dict:
        #grabs top 10 passwords for country
        top = df.loc[(df["country_code"] == country) & (df["Rank"] < 11), "Password"]
        print(f'These are the top 10 passwords for the country {dict[country]}:\n{top.to_string()}')


def main():
    #dict of countries in the data.csv
    #allows the user input to be checked for valid country without have to go through the csv file
    countries = {"au": "Australia", "at":"Austria", "be":"Belgium", "br":"Brazil", "ca":"Canada",
    "cl":"Chile", "cn":"China", "co":"Colombia", "cz":"Czech Republic", "dk":"Denmark", "ee":"Estonia", 
    "fi":"Finland", "fr":"France", "de":"Germany", "gr":"Greece", "hu":"Hungary", "in":"India", 
    "id":"Indonesia", "ie":"Ireland", "il":"Israel", "it":"Italy", "jp":"Japan", "kr":"Korea", 
    "lv":"Latvia", "lt":"Lithuania", "my":"Malaysia", "mx":"Mexico", "nl":"Netherlands", "nz":"New Zealand", 
    "ng":"Nigeria", "no":"Norway", "ph":"Philippines", "pl":"Poland", "pt":"Portugal", "ro":"Romania", 
    "ru":"Russia", "sa":"Saudi Arabia", "sk":"Slovak Republic", "za":"South Africa", "es":"Spain", 
    "se":"Sweden", "ch":"Switzerland", "th":"Thailand", "tr":"Turkey", "ua":"Ukraine", 
    "ae":"United Arab Emirates", "gb":"United Kingdom", "us":"United States", "vn":"Vietnam"}

    #create the dataframe for answering questions, passed to functions
    df = pd.read_csv("data.csv")

    #start while loop for menu options
    ask = 0
    while ask != 'q':
        printOptions()
        ask = str(input("Which question do you want answered? ")).lower()

        if ask == '1':
            answerOne(df)
            print()
        elif ask == '2':
            answerTwo(df, countries)
            print()
        elif ask == '3':
            answerThree(df, countries)
            print()
        elif ask == '4':
            answerFour(df, countries)
            print()
        elif ask == 'q':
            break
        else:
            print(f"{ask} was an invalid input. Try again.")

main()