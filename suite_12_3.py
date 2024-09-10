import unittest
import tests_12_1
import tests_12_2

runTest = unittest.TestSuite()

runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTest)

