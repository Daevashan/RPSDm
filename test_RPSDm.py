import unittest
import RPSDm

class MyTestCase(unittest.TestCase):
    
    def test_validUserInput(self):
        validInput = ["rock", "paper", "scissors"]
        user_inputValue = RPSDm.user_input()
        self.assertTrue(user_inputValue in validInput)
        
    def test_validRobotInput(self):
        validInput = ["rock", "paper", "scissors"]
        robot_inputValue = RPSDm.robot_input()
        self.assertTrue(RPSDm.robot_input in validInput)
        
    def test_battleUserRock(self):
        resultReturned_tie = RPSDm.battleResults("rock", "rock")
        resultReturned_win = RPSDm.battleResults("rock", "scissors")
        resultReturned_lose = RPSDm.battleResults("rock", "paper")
        self.assertEqual("You Drew!", resultReturned_tie)
        self.assertEqual("You Win!", resultReturned_win)
        self.assertEqual("You Lost!", resultReturned_lose)
        
    def test_battleUserPaper(self):
        resultReturned_tie = RPSDm.battleResults("paper", "paper")
        resultReturned_win = RPSDm.battleResults("paper", "rock")
        resultReturned_lose = RPSDm.battleResults("paper", "scissors")
        self.assertEqual("You Drew!", resultReturned_tie)
        self.assertEqual("You Win!", resultReturned_win)
        self.assertEqual("You Lost!", resultReturned_lose)
        
    def test_battleUserScissors(self):
        resultReturned_tie = RPSDm.battleResults("scissors", "scissors")
        resultReturned_win = RPSDm.battleResults("scissors", "paper")
        resultReturned_lose = RPSDm.battleResults("scissors", "rock")
        self.assertEqual("You Drew!", resultReturned_tie)
        self.assertEqual("You Win!", resultReturned_win)
        self.assertEqual("You Lost!", resultReturned_lose)
        

if __name__ == '__main__':
    unittest.main()