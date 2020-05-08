import unittest
import MathFunctions 

class KnownValues(unittest.TestCase):
    #Test areacircle() pi r^2
    def test_areaCircle_for_10radius(self):
        #Now we will capture the results of the function
        result = MathFunctions.areaCircle(10)
        #CHECK FOR expected output
        expected = 314.1592653589793
        self.assertEqual(expected, result)
    def test_areaCircle_for_2radius(self):
        #Captures the results of the function
        result = MathFunctions.areaCircle(2)
        #Check for output
        expected = 12.566370614359172
        self.assertEqual(expected, result)


#Run the test
if __name__ == '__main__':
    unittest.main()