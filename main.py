import random
from enum import Enum
import pandas as pd

class Marble(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Bowl:
    def __init__(self, name):
        self.name = name
        self.size = 10
        self.marbles = []

    def __repr__(self):
        summary = dict()
        summary['marbles'] = [Marble.RED, Marble.BLUE, Marble.GREEN, "Total"]
        summary['count'] = [self.get_number_of_marbles(Marble.RED),
                            self.get_number_of_marbles(Marble.BLUE),
                            self.get_number_of_marbles(Marble.GREEN),
                            len(self.marbles)]
        dataframe = pd.DataFrame(summary)
        print(f"--- {self.name} ---")
        print(dataframe)
        print("---")
        return self.name

    def get_total_number_of_marbles(self):
        return len(self.marbles)

    def get_number_of_marbles(self, marble):
        return self.marbles.count(marble)

    def add_a_marble(self, marble):
        if self.get_total_number_of_marbles() >= self.size:
            print("Bowl full")
            return
        self.marbles.append(marble)

    def get_a_marble(self):
        idx = random.randint(0, self.get_total_number_of_marbles()-1)
        return self.marbles[idx]


class SpinningTable:
    def __init__(self):
        self.name = "spinning table"
        self.size = 10
        self.bowl_holder = list()
        self.index = 0

    def __repr__(self):
        summary = dict()
        summary['bowl'] = []
        summary['count'] = []
        total_marbles = 0
        for bowl in self.bowl_holder:
            summary['bowl'].append(bowl.name)
            summary['count'].append(bowl.get_total_number_of_marbles())
            total_marbles += bowl.get_total_number_of_marbles()
            print(bowl)

        summary['bowl'].extend(["Total Marbles"])
        summary['count'].extend([total_marbles])
        dataframe = pd.DataFrame(summary)
        print(f"--- {self.name} ---")
        print(dataframe)
        print("---")
        return self.name

    def add_a_bowl(self, bowl):
        self.bowl_holder.append(bowl)

    def spin(self):
        self.index = random.randint(0, len(self.bowl_holder)-1)


def print_summary(bowl):
    summary = dict()
    summary['marbles'] = [Marble.RED, Marble.BLUE, Marble.GREEN, "Total"]
    summary['count'] = [2, 1, 1]
    dataframe = pd.DataFrame(summary)
    print(dataframe)

def main():
    bowl1 = Bowl(name="bowl1")
    for _ in range(0, 2):
        bowl1.add_a_marble(Marble.RED)
    bowl1.add_a_marble(Marble.BLUE)
    bowl1.add_a_marble(Marble.GREEN)

    bowl2 = Bowl(name="bowl2")
    for _ in range(0, 3):
        bowl2.add_a_marble(Marble.RED)
    for _ in range(0, 3):
        bowl2.add_a_marble(Marble.BLUE)
    for _ in range(0, 1):
        bowl2.add_a_marble(Marble.GREEN)

    bowl3 = Bowl(name="bowl3")
    for _ in range(0, 2):
        bowl3.add_a_marble(Marble.RED)
    for _ in range(0, 0):
        bowl3.add_a_marble(Marble.BLUE)
    for _ in range(0, 3):
        bowl3.add_a_marble(Marble.GREEN)

    spinning_table = SpinningTable()
    spinning_table.add_a_bowl(bowl1)
    spinning_table.add_a_bowl(bowl2)
    spinning_table.add_a_bowl(bowl3)
    print(spinning_table)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

