import unittest
import Komodo_Claim_Department

class TestClaim(unittest.TestCase):

    def test_Add_A_Claim_should_add_claim(self):
        self.ClaimID = 'ClaimID'
        self.ClaimType = 'ClaimType'
        self.Description = 'Description'
        self.ClaimAmount = 'ClaimAmount'
        self.DateOfIncident = 'DateOfIncident'
        self.DateOfClaim = 'DateOfClaim'
        self.IsValid = 'IsValid'

        #act
        Komodo_Claim_Department.Add_A_Claim(self.ClaimID, self.ClaimType, self.Description, self.ClaimAmount, self.DateOfIncident, self.DateOfClaim, self.IsValid) 
        actual = len(Komodo_Claim_Department.number_of_claims)
        expected = 1

        #assert
        self.assertEqual(expected, actual)

    def test_list_of_claim_should_View_Claim(self):
        #arrange
        #act
        actual = len(Komodo_Claim_Department.number_of_claims) 
        expected = 1 
        #assert
        self.assertEqual(expected, actual)

    def test_pick_a_claim_should_give_next_claim(self):
        self.ClaimID = 'ClaimID'
        self.ClaimType = 'ClaimType'
        self.Description = 'Description'
        self.ClaimAmount = 'ClaimAmount'
        self.DateOfIncident = 'DateOfIncident'
        self.DateOfClaim = 'DateOfClaim'
        self.IsValid = 'IsValid'

        #act
        Komodo_Claim_Department.Add_A_Claim(self.ClaimID, self.ClaimType, self.Description, self.ClaimAmount, self.DateOfIncident, self.DateOfClaim, self.IsValid)
        self.assertTrue(Komodo_Claim_Department.number_of_claims.pop())       


