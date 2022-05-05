# class contains a list of ServiceDay objects, one for each day of the the dog walking service is in business
from Dog_pt_10 import Dog
from ServiceDay import ServiceDay
import random


class DogWalkingService2:
    __days = []  # -> ServiceDay ( contains available service days )

    def __init__(self, capacity, number_of_days):
        """initialized how many days the service will run (from user input) and also the initialize capacity
        for each day the service runs"""

        for i in range(number_of_days):
            self.__days.append(ServiceDay(capacity))
        for j in range(len(self.__days)):
            self.enrollDog(Dog())

    def enrollDog(self, dog: Dog) -> bool:
        """ Method adds a dog to the ServiceDay object at the end of the days list """
        return self.__days[-1].enrollDog(dog)

    def removeDog(self, index: int) -> Dog:
        """ Method removes a dog from the ServiceDay object at the end of the days list """
        return self.__days[index].removeDog(1)

    def processDay(self, number_of_walks: int) -> None:
        """ Method conducts the specified number of walks on the ServiceDay object at the end of the days list if walk
         includes 2 or all dogs is random"""
        number_of_dogs = random.randint(0, 1)  # randomly walking 2 or all dogs
        is_it_fast_walk = random.randint(0, 1) == 0

        # randomly determining if 2 or all dogs will walk that service day
        if number_of_dogs == 0:
            self.__days[-1].walk2Dogs(is_it_fast_walk)  # method that walks only 2 dogs -> from ServiceDay
        else:
            self.__days[-1].walkAllDogs(is_it_fast_walk)  # method that walks all dogs -> from ServiceDay

        for j in range(number_of_walks):
            is_it_fast_walk = random.randint(0, 1) == 0
            number_of_dogs = random.randint(0, 1)  # randomly walking 2 or all dogs
            if number_of_dogs == 0:
                self.__days[-1].walk2Dogs(is_it_fast_walk)  # method that walks only 2 dogs -> from ServiceDay
            else:
                self.__days[-1].walkAllDogs(is_it_fast_walk)  # method that walks all dogs -> from ServiceDay
        day = ServiceDay(self.__days[-1].getNumberOfDogs())
        for dog in self.__days[-1].getDogs():
            day.enrollDog(dog)
        self.__days.append(day)   # new ServiceDay object added to days list with all same dogs enrolled

    def getDaySummary(self, days: int) -> str:
        return self.__days[days].getSummary()

    def getSummary(self) -> str:
        """Method gets the necessary values to create a summary of how long the walking service was active
        along with average number of walks taken per day, average minutes per walk, and average minutes per day.
        Along with the success rate for dogs that pooped"""
        success_count = 0
        total_walks = 0
        total_min = 0
        days = len(self.__days)
        dog_stats = {}
        total_pees = 0
        total_poops = 0
        summary_of_dogs = ''
        num = 1
        for i in range(days):
            success_count += self.__days[i].getSuccessCount()
            total_walks += self.__days[i].getNumberOfWalks()
            total_min += self.__days[i].getTotalMinutesWalked()
            for dog in self.__days[i].getDogs():
                total_pees += dog.getTotalPees()
                total_poops += dog.getTotalPoops()
                dog_stats[dog.getName()] = (dog.getWalkerType(), total_pees, total_poops)
                summary_of_dogs += f'{num}. {dog.getName} is a {dog_stats[dog.getName()[0]]} who peed ' \
                                   f'{dog_stats[dog.getName()[1]]} and pooped {dog_stats[dog.getName()[3]]} ' \
                                   f'{dog.makePluralIfAppropriate("time")}.\n'
                num += 1
        success_rate = (success_count / days) * 100  # percentage rate of successful walks (where all dogs pooped)
        avg_min_walk = total_min / total_walks  # average minutes per walk
        avg_walk = total_walks/days    # average number of walks per day
        avg_min_day = total_min/days  # average minutes per day

        return f'/n{success_rate}% of the walks were successful (all dogs pooped)\nAverage number of walks per day: ' \
               f'{avg_walk} walks\nAverage minutes per walk: {avg_min_walk}\n Average minutes per day: ' \
               f'{avg_min_day} minutes\nHere is a summary of all the dogs still enrolled in the service: ' \
               f'{summary_of_dogs}'

