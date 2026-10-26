# Week 1.5, Session 2: Task 5

import math

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data = []
        with open(filename) as file:
            self.data.append(file.readlines())
            for i in self.data:
                i.strip()
                print(i)

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        return (sum(self.data) / len(self.data))

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        sorted_data = sorted(self.data)
        midpoint = len(sorted_data) / 2
        if len(sorted_data) % 2 == 0:
            return (self.data[math.floor(midpoint)] + self.data[math.ceil(midpoint)])
        elif len(sorted_data) == 1:
            return self.data[0]
        elif len(sorted_data == 0):
            return -999
        else:
            return self.data[midpoint]