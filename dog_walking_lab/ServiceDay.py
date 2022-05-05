import random
from Dog_pt_10 import Dog


class ServiceDay:

    def __init__(self, capacity: int):
        self.dogs = []  # used to keep track of all the dogs managed by the dog walking service
        self.numberOfDogs = capacity * 1.25  # support 25% more dogs than the user would like to walk
        self.successCount = 0
        self.numberOfWalks = 0
        self.totalMinutes = 0

    def enrollDog(self, dog: Dog) -> bool:
        """Method enrolls dogs and makes sure to check that the capacity allowed
         doesn't exceed what was indicated by user"""

        if len(self.dogs) != self.numberOfDogs:
            self.dogs.append(dog)  # adds dog to service
            return True  # method returns true if and only if the dog was added to the dog walking service
        return False  # if max capacity is reached then we return false and no more dogs can be enrolled

    def removeDog(self, index: int) -> Dog:
        """Method removes a specific dog from the list using index position,
         used pop() to then return what dog was removed"""
        return self.dogs.pop(index)

    def getSummary(self) -> str:
        """ Method is suppose to run through all the dogs in the service and get back a description of their last
        walks. """
        summary = ''
        for dog in self.dogs:
            summary += f'\n{dog.getName()} is a {dog.getWalkerType()} walker who peed {dog.getTotalTimesPeed()} ' \
                       f'{dog.makePluralIfAppropriate(dog.getTotalTimesPeed(),"time")} ' \
                       f'and pooped {dog.getTotalTimesPooped()} ' \
                       f'{dog.makePluralIfAppropriate(dog.getTotalTimesPooped(),"time")}'
        summary += f'\n\nWe gave {self.numberOfWalks} walks for a total of {self.totalMinutes} minutes of walking time'
        return summary

    def walk2Dogs(self, is_fast=False) -> bool:
        """This method simulate the dog walk by calling method walk from Dog class and also determining the success
        of the walk """
        minutes = random.randint(10, 45)
        dog1 = self.dogs[-1]
        dog2 = self.dogs[-2]

        pace1 = dog1.walk(minutes, is_fast)
        pace2 = dog2.walk(minutes, is_fast)
        self.numberOfWalks += 1
        self.totalMinutes += minutes  # update time spent for walking to total
        if pace1 and pace2:
            self.successCount += 1
            return True
        elif pace2:
            self.successCount += 1
            return True
        else:
            return False

    def walkAllDogs(self, is_fast) -> bool:
        minutes = random.randint(10, 45)
        for dog in self.dogs:
            pace = dog.walk(minutes, is_fast)
            self.numberOfWalks += 1
            self.totalMinutes += minutes
            if pace:
                self.successCount += 1
        return True

    def getNumberOfWalks(self) -> int:
        return self.numberOfWalks

    def getTotalMinutesWalked(self) -> int:
        return self.totalMinutes

    # This is a method (accessor) which accesses a private variable
    def getDogs(self):  # type array
        return self.dogs

    def getNumberOfDogs(self) -> int:
        """Method returns how many dogs are currently enrolled"""
        return len(self.dogs)

    def getSpacesLeft(self) -> int:
        """Method returns how many additional dogs can be enrolled before service reaches capacity"""
        return int(self.numberOfDogs - len(self.dogs))

    def getSuccessCount(self):
        return self.successCount
