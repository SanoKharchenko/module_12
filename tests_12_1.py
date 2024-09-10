import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run = runner.Runner('test_walk')
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = runner.Runner('test_run')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = runner.Runner('tester_1')
        run_2 = runner.Runner('tester_2')
        for i in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()
