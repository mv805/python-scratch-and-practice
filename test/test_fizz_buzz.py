import unittest
from fizz_buzz.fizz_buzz import fizzBuzz


class TestPast(unittest.TestCase):

    def test_fizz_buzz(self):
        # self.assertEqual(fizzBuzz(10), 10)

        test_cases = [
            (3, ["1", "2", "Fizz"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
             "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
        ]
        # test_cases = [
        #     (0, 1, 1, 61000),
        #     (1, 1, 1, 3661000),
        #     (0, 0, 0, 0),
        #     (1, 0, 1, 3601000),
        #     (1, 0, 0, 3600000),
        # ]

        for case in test_cases:
            n, stringArrayResult = case
            with self.subTest(f"Input (n):{n}, Result:{stringArrayResult}"):
                self.assertEqual(fizzBuzz(n), stringArrayResult)


if __name__ == '__main__':
    unittest.main()
