import pandas as pd
import os

curr_ = os.path.dirname(__file__)
path = os.path.join(curr_,"atm.CSV")

df = pd.read_csv(path)


df.set_index(df.columns[0],inplace =True)

def total_amount(df):

    total = df["Amount of Frauds (in Rs. crore)"].sum()
    print(f"Total amount  involved in ATMs frauds in last 6 years in india is RS.{total} cr")


def number_of_atms(df):
    yr = input("Enter the desired year for no.of atms :")
    atms = df.loc[yr,'Number of atms']
    print(f"No.of atms in {yr} are {atms}")
    
    
def yearly_fraud_amount(df):

    yr = input("Enter the required year for amount involved in frauds:")
    amount = df.loc[yr,"Amount of Frauds (in Rs. crore)"]
    print(f"amount involved in ATMs frauds in {yr} is RS.{amount}cr")
    

def total_atms(df):

    n=len(df['Number of atms'])

    total = df['Number of atms'].iloc[n - 1]
    print(f"Total no.of atms in india present are {total}")


def efficient_year(df):

    df['ratio'] = df["stolen amount(in Rs.crore)"]/df["Number of atms"]

    min = df['ratio'].min()
    row_number = df[df['ratio'] == min].index[0]
    print(f"the most efficient year {row_number}")

def Total_amount_stolen(df):

    total = df["stolen amount(in Rs.crore)"].sum()
    print(f"Total amount stolen from ATMs in last 6years in india is {total}")

def main():
    print("Select one option from below : ")
    print("""    1.Total amount involved in ATMs frauds in last 6 years. 
    2.Number of atms in the year. 
    3.Amount involved in ATMs frauds in the year. 
    4.Total no.of atms in india. 
    5.Efficient year(less stolen amount/Number of atms ratio)
    6.Total amount stolen from ATMs in last 6years in india""" )
    option = int(input("Enter the option (enter number): "))
    if option == 1:
        total_amount(df)
    elif option == 2:
        number_of_atms(df)
    elif option == 3:
        yearly_fraud_amount(df)
    elif option == 4:        
        total_atms(df)

    elif option == 5:
        efficient_year(df)
    elif option == 6:
        Total_amount_stolen(df)
main()