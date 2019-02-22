
class Claim:

    def __init__(self, ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid):
        self.ClaimID = ClaimID
        self.ClaimType = ClaimType
        self.Description = Description
        self.ClaimAmount = ClaimAmount
        self.DateOfIncident = DateOfIncident
        self.DateOfClaim = DateOfClaim
        self.IsValid = IsValid

    def __repr__(self):
        return f"{self.ClaimID}- {self.ClaimType}- {self.Description}- {self.DateOfClaim}- {self.DateOfIncident}- {self.IsValid}"
        
if __name__ == "__main__":
    car = Claim('3', 'car', 'accident', '$200', '2/2/2222', '2/18/2222', 'IsValid')
    print(car)



 
