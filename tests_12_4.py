import logging
from rt_with_exceptions import Runner
import unittest


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename="runner_tests.log",
                            level=logging.INFO,
                            filemode="w",
                            encoding='utf-8',
                            format="%(levelname)s | %(message)s")

    def test_walk(self):
        try:
            runner = Runner("Vasya", -3)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info("'test_walk' passed successfully")
        except ValueError:
            logging.warning("Incorrect speed for Runner", exc_info=True)

    def test_run(self):
        try:
            runner = Runner(86167)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info("'test_run' passed successfully")
        except TypeError:
            logging.warning("Incorrect data type for Runner", exc_info=True)

    def test_challenge(self):
        run_1 = Runner('Vasya')
        run_2 = Runner('Petya')
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == "__main__":
    unittest.main()

