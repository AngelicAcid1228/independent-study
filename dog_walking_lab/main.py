import random

from Dog_pt_10 import Dog
from ServiceDay import ServiceDay  # renamed what was previously DogWalkingService -> ServiceDay
from DogWalkingService_pt_10 import DogWalkingService2

if __name__ == '__main__':

    dog_amount = int(input('How many dogs would you like to start with:  '))

    days_amount = int(input('How many days would you like the service to run: '))
    dog_service = DogWalkingService2(days_amount, dog_amount)  # fill in array of how many days user would like
    # service to run
    for i in range(dog_amount):
        dog_service.enrollDog(Dog())

    for day in range(1, days_amount + 1):

        isItFastWalk = random.randint(0, 1) == 0

        if day % 3 == 0:
            '''Every third day, the dog that was enrolled the longest ago is removed from the current service day'''
            dog_service.removeDog(0)
        if day % 5 == 0:
            '''Every fifth day, two additional dogs are enrolled in the current service day'''
            dog_service.enrollDog(2)

        walk_amount = random.randint(2, 6)  # 2 to 6 walks (randomly determined) each day
        dog_service.processDay(walk_amount)  # passing random walk number that will be done that day

    print('The dog walking service was active for ', days_amount)
    print(dog_service.getSummary())

'''
    for walkNum in range(1, walk_amount + 1):
        # randomizing how many dogs will be walked and if they like fast or slow walks
        choiceWalk = random.randint(0, 1)
        isItFastWalk = random.randint(0, 1) == 0

        if choiceWalk == 0:
            print(f'Walk {walkNum}:')
            user.walk2Dogs(isItFastWalk)  # randomizes if it will be a fast walk or slow one

            dog1 = user.getDogs()[-1]
            dog2 = user.getDogs()[-2]

            print(dog1.getDescriptionOfLastWalk())
            print(dog2.getDescriptionOfLastWalk())

        elif choiceWalk == 1:
            print(f'Walk {walkNum}:')
            user.walkAllDogs(isItFastWalk)
            allDogs = user.getDogs()
            for dog in allDogs:
                print(dog.getDescriptionOfLastWalk())

    print(user.getSummary())
'''
