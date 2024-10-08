import logging
import unittest
from pypyfile import Runner, Tournament

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s',
                    filename='runner_tests.log',
                    filemode='w',
                    encoding='UTF-8')

class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner("Бегун")

    def test_run(self):
        try:
            r2 = Runner(2)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")

    def test_walk(self):
        try:
            r1 = Runner('Вася', -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")

    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)

class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_first_tournament(self):
        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()
        self.assertEqual(results[max(results.keys())], "Ник")

    def test_second_tournament(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()
        self.assertEqual(results[max(results.keys())], "Ник")

    def test_third_tournament(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()
        self.assertEqual(results[max(results.keys())], "Ник")

if __name__ == '__main__':
    unittest.main()