answer = input("What woul you like to play?? (yes/no)")
if answer.lower().strip() == "yes":
    answer = input("You reach a crossroad, would you like to left or right??").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack.")

        if answer == "attack":
            print("That was not a greatest idea, you lost!")
        else: 
            print("Good Choice!!, you made it away safely.")

            answer = input("you see a car and a plane. Which would you like to take?? (car/plane)")

            if answer == "plane":
                print("Unfortunately you do not know how to fly...Game Over!!")
            else:
                print("You won!!, as you know driving and get back to your home")


    elif answer == "right":
        print("You walk aimlessly to the right and fall on a patch of ice. you injured your leg and can't continue..Game Over!!")

    else:
        print("invalid choice , you lost!!")

else:
    print("That's to bad!!")