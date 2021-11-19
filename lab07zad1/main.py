class FizzBuzz:
    def game(self, *args):
        if len(args) == 1:
            num = args[0]
            fb = ""
            if type(num) == int:
                if num % 5 == 0 or num % 3 == 0:
                    if num % 3 == 0:
                        fb = fb + "Fizz"
                    if num % 5 == 0:
                        fb = fb + "Buzz"
                    return fb
                else:
                    raise Exception("Error in FizzBuzz")
            else:
                raise Exception("Error in FizzBuzz")
        else:
            raise ValueError("Wrong number of arguments")

    def gameWithDocString(self, x):
        """Returnes Fizz when n is divisible by 3, Buzz when n is divisible by 5 and FizzBuzz when n is divisible by 15
        >>> f = FizzBuzz()
        >>> f.game(1)
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest main.FizzBuzz.gameWithDocString[1]>", line 1, in <module>
            f.addWithDocString(1)
          File "D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab07/lab07zad1/main.py", line 38, in addWithDocString
            raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> f.game(25)
        'Buzz'
        >>> f.game(165)
        'FizzBuzz'
        >>> f.game(33)
        'Fizz'
        >>> f.game(1.5656)
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest main.FizzBuzz.gameWithDocString[1.5656]>", line 1, in <module>
            f.addWithDocString(5)
          File "D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab07/lab07zad1/main.py", line 38, in addWithDocString
            raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> f.game({})
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest main.FizzBuzz.gameWithDocString[6]>", line 1, in <module>
            f.addWithDocString({})
          File "D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab07/lab07zad1/main.py", line 38, in addWithDocString
            raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> f.game(-15)
        'FizzBuzz'
        >>> f.game()
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest main.FizzBuzz.gameWithDocString[8]>", line 1, in <module>
            f.game()
          File "D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab07/laboratorium-7-Justyna7/lab07zad1/main.py", line 18, in game
            raise ValueError("Wrong number of arguments")
        ValueError: Wrong number of arguments
        >>> f.game(16, 4)
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest main.FizzBuzz.gameWithDocString[9]>", line 1, in <module>
            f.game(16, 4)
          File "D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab07/laboratorium-7-Justyna7/lab07zad1/main.py", line 18, in game
            raise ValueError("Wrong number of arguments")
        ValueError: Wrong number of arguments
        """


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'f': FizzBuzz()})

# Odpalenie: python3 main.py -v