import random
from numpy import random


class Dog:
    dogNameList = ['Sally', 'Po', 'Spot', 'Alex', 'Smith', 'Noodle',
                   'Kiki', 'Rue', 'Teddy', 'Nina', 'Charlie', 'Milo', 'Daisy', 'Louie']

    # when it says {read only} that means
    # it is final ( no more changes can be made )

    def __init__(self):
        self.name = random.choice(self.dogNameList)  # will choose a dog name randomly from the list
        self.prefersFastWalks = random.randint(0, 2) == 1
        self.isLastWalkFast = True  # was the last walk fast or not
        self.solidProductionRate = random.uniform(0, 0.2)
        self.totalWalks = 0
        self.totalTimesPeed = 0
        self.totalTimesPooped = 0
        self.liquidProductionRate = random.uniform(0, 0.2)
        self.LastMinutes = 0  # last walk

    def getName(self) -> str:
        return self.name

    def walk(self, length_in_minutes: int, is_fast: bool) -> bool:
        """
          Conducts the walk for the dog instance, should modify the solid production rate, the totalTimesPooped, and
          the totalTimesPeed. Should return whether or not the dog enjoyed the walk.
          :param length_in_minutes: The time the walk took
          :param is_fast: The speed of the walk.
          """
        self.LastMinutes = length_in_minutes
        avg_poop = self.solidProductionRate * length_in_minutes
        self.totalTimesPooped += random.poisson(lam=avg_poop, size=None)

        avg_pee = self.liquidProductionRate * length_in_minutes
        self.totalTimesPeed += random.poisson(lam=avg_pee, size=None)

        self.totalWalks += 1
        self.isLastWalkFast = is_fast
        return self.prefersFastWalks == is_fast  # returns if the dog liked the fast walk or not

    def getNumberOfWalks(self) -> int:
        return self.totalWalks

    def getTotalTimesPeed(self) -> int:
        return self.totalTimesPeed

    def getTotalTimesPooped(self) -> int:
        return self.totalTimesPooped

    def getWalkerType(self) -> str:
        if self.prefersFastWalks:
            return 'fast'
        elif not self.prefersFastWalks:
            return 'slow'

    def getDescriptionOfLastWalk(self) -> str:
        """Method provides the last description of dogs walks"""
        if self.isLastWalkFast:
            if self.prefersFastWalks and self.totalTimesPooped >= 1:
                return f'{self.getName()} went on a fast {self.LastMinutes} minute walk and even pooped.'
            elif self.prefersFastWalks and self.totalTimesPooped == 0:
                return f'{self.getName()} went on a fast {self.LastMinutes} minute walk.'
            else:
                return f'{self.getName()} is a slow walker and refused to go on this fast walk'
        elif not self.isLastWalkFast:
            if self.prefersFastWalks and self.totalTimesPooped >= 1:
                return f'{self.getName()} went on a slow {self.LastMinutes} minute walk but did not enjoy it.'
            elif self.prefersFastWalks and self.totalTimesPooped == 0:
                return f'{self.getName()} went on a slow {self.LastMinutes} minute walk but did not enjoy it.'
            elif not self.prefersFastWalks and self.totalTimesPooped >= 1:
                return f'{self.getName()} went on a slow {self.LastMinutes} minute walk and even pooped.'
            elif not self.prefersFastWalks and self.totalTimesPooped == 0:
                return f'{self.getName()} went on a slow {self.LastMinutes} minute walk.'

    @staticmethod  # static method knows nothing about the class and just deals w/ the parameters
    def makePluralIfAppropriate(quantity: int, word: str) -> str:
        """Method checks whether or not the quantity amount passed in changes the work time to times or keeps it time
         """
        if quantity == 1:
            return word
        elif quantity > 1 or quantity == 0:
            return word + 's'
