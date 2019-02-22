
import claim 

number_of_claims = []

def Add_A_Claim(ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid):
    C = claim.Claim(ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid)
    number_of_claims.append(C)

def list_of_claim():
     if len(number_of_claims) > 0:
          print(number_of_claims)
     else:
          print('list Empty')

def Pick_A_claim():
     if len(number_of_claims) > 0:
          print(number_of_claims)
     else:
          print('There is nomore claim')
          exit()
     user = input('Do you want to work on this: Yes/No ').capitalize()
     if user == 'Yes':
          number_of_claims.pop()
          print('You got an Assignment')


     







