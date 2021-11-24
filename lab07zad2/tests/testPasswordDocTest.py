import sys
sys.path.insert(1, '..')
from main import *


class testPasswordDoc:
    def testValidPasswordWithDocString(self):
        """Returns True if Pass is >=8 characters long, has atl least one lowercase letter, uppercase letter, number and other nonwhite character
        >>> f = Password()
        >>> f.ValidPassword(1)
        False
        >>> f.ValidPassword("25a.A5-a")
        True
        >>> f.ValidPassword("25a.c5-a")
        False
        >>> f.ValidPassword('fghgvbhnjkvb')
        False
        >>> f.ValidPassword('234567890')
        False
        >>> f.ValidPassword({})
        False
        >>> f.ValidPassword('-1Ab')
        False
        >>> f.ValidPassword('AhajjXFGHJI')
        False
        >>> f.ValidPassword('zsxdfghjkljhytre')
        False
        >>> f.ValidPassword('4AhajjX9FGHJI')
        False
        >>> f.ValidPassword('zsx4dfghjkl7jhy0tre')
        False
        >>> f.ValidPassword('Aha_jjXFGHJI')
        False
        >>> f.ValidPassword('zsxdfghjklj_hytre')
        False
        >>> f.ValidPassword('Ah9a_jjX7FGHJI')
        True
        """


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'f': Password()})
