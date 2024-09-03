import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        cursor = Runner('Igor')
        for walk in range(10):
            cursor.walk()
        self.assertEqual(cursor.distance, 50)

    def test_run(self):
        cursor = Runner('Vasya')
        for run in range(10):
            cursor.run()
        self.assertEqual(cursor.distance, 100)

    def test_challenge(self):
        cursor1 = Runner('Petya')
        cursor2 = Runner('Vanya')
        for move in range(10):
            cursor1.walk()
            cursor2.run()
        self.assertNotEqual(cursor1.distance, cursor2.distance)


if __name__ == "__main__":
    unittest.main()
