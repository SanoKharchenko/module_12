import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner_2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(runner) for key, runner in result.items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result1 = tour1.start()
        last_runner1 = list(result1.values())
        self.assertTrue(last_runner1[-1] == 'Ник')
        self.all_results['test_1'] = result1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tour2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result2 = tour2.start()
        last_runner2 = list(result2.values())
        self.assertTrue(last_runner2[-1] == 'Ник')
        self.all_results['test_2'] = result2

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tour3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result3 = tour3.start()
        last_runner3 = list(result3.values())
        self.assertTrue(last_runner3[-1] == 'Ник')
        self.all_results['test_3'] = result3


if __name__ == '__main__':
    unittest.main()
