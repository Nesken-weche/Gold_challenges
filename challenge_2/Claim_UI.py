
import Komodo_Claim_Department

def Add_Claim():
    ClaimID = int(input('Enter a claim ID: '))
    ClaimType = input('Enter a claim Type such as Car, Home, Theft: ').capitalize() 
    Description = input('Enter a brief description such as accident: ') 
    ClaimAmount = int(input('Enter a claim amount:$ ')) 
    DateOfIncident = input('Enter date such as feb, 2 18=> 02/02/18: ') 
    DateOfClaim = input('Enter date as such feb 2, 18=> 02/02/18: ') 
    IsValid = input('Enter True if DateOfClaim is less than 30 days from Date of Incident: ')
    Komodo_Claim_Department.Add_A_Claim(ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid)

def View_Claim():
    Komodo_Claim_Department.list_of_claim()

def Next_claim():
    Komodo_Claim_Department.Pick_A_claim()
    
choices = {
    "1" : Add_Claim,
    "2" : View_Claim,
    "3" : Next_claim,
    "4" : exit
}

while True:
    print('welcome To Komodo Claim Department')
    user_input = input('1. Add Claim\n' +
                    '2. View Claim\n' +
                    '3. Next Claim\n' +
                    '4. Exit\n')
    action = choices.get(user_input)
    if action:
        action()
    else:
        print("Input not valid")

'''

while True:
    print('welcome To Komodo Claim Department')
    user_input = input('1. View Claim\n' +
                    '2. Next Claim\n' +
                    '3. Add Claim\n' +
                    '4. Exit\n')

    if user_input == '1':
        Number_of_claims = Komodo_Claim_Department.View_Claim()
        print(Number_of_claims)
    elif user_input == "2":
        Number_of_claims = Komodo_Claim_Department.Next_claim()
        for items in Number_of_claims:
            print(items)
    elif user_input == "3":
        ClaimID = int(input('Enter a claim ID: '))
        ClaimType = input('Enter a claim Type such as Car, Home, Theft: ').capitalize() 
        Description = input('Enter a brief description such as accident: ') 
        ClaimAmount = int(input('Enter a claim amount:$ ')) 
        DateOfIncident = input('Enter date such as feb, 2 18=> 02/02/18: ') 
        DateOfClaim = input('Enter date as such feb 2, 18=> 02/02/18: ') 
        IsValid = input('Enter True if DateOfClaim is less than 30 days from Date of Incident: ')
        Komodo_Claim_Department.Add_Claim(ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid)
    elif user_input == "4":
        exit(0)
'''
