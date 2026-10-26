# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth: date):
        """constructor
        args: name (string), birthday (date)
        returns: none.
        validates that the name and birthday are correctly specified.
        """
        if not isinstance(name, str):
            raise TypeError("name should be a string.")
        if not isinstance(birth, date):
            raise TypeError("birth should be a date.")
        if name == "":
            raise ValueError("name should not be an empty string.")
        self.name = name
        self.birthday = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """initials
        args: none
        returns: string
        Returns a string consisting of the person's initials.
        """
        names = self.name.split(' ')
        initials = ""
        for n in names:
            initials += n[0].capitalize()
        return initials
        
    def is_birthday(self):
        """
        is_birthday(). 
        args: none
        returns: boolean.
        if today is the person's birthday, return true. Otherwise, return false.
        """
        if date.today() == self.birthday:
            return True
        return False