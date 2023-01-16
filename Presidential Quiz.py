lives = True


print("Welcome to Ahmed's U.S Presidential Quiz!")
print("Please enter your name!")
userName = input()

print("Nice to meet you", userName,)
print("Today you'll be taking a quiz on which U.S President served first out of three options!")
print("You'll have only three chances to mess up! Let's get started!")



while lives:
    
    def lifeCount():
        if livesRemaining == 0:
            print("You're out of lives! Good luck trying again!")
            quit()


    livesRemaining = 3
    
    if livesRemaining == 0:
        quit()

    presidents = ["George Washington","John Adams","Thomas Jefferson","James Maddison","James Monroe","John Quincy Adams",
        "Andrew Jackson","Martin Van Buren","William Henry Harrison","James K. Polk","Zachary Taylor","Franklin Pierce","James Buchanan","Abraham Lincoln",
        "Ulysses S. Grant","Rutherford B. Hayes","James A. Garfield ","Grover Cleveland","Herbert Hoover","Calvin Coolidge","Franklin D. Roosevelt","Harry S. Truman",
        "Dwight D. Eisenhower","John F. Kennedy","Richard Nixon","Jimmy Carter","Ronald Reagan","Bill Clinton","George W. Bush","Lyndon B. Johnson"]

    
    print("Choose either number 1 2 or 3 on your keyboard!" "\n Question 1: \n 1. George Washington \n 2. Martin Van Buren \n 3. James Monroe")

    response = input() 

    if response == "1":
        print("Correct! 1/10!")  
    else:
        livesRemaining -= 1
        print("Incorrect!")
        lifeCount()

    print("Question 2: \n 1. James Madison \n 2. Andrew Jackson \n 3. John Quincy Adams")
    response = input()
    if response == "1": 
        print("Correct! 2/10!")
    else:
        livesRemaining -= 1
        print("Incorrect!")
        lifeCount()
    
    print("Question 3: \n 1. Abraham Lincoln \n 2. Zachary Taylor \n 3. James Buchanan")
    response = input()
    if response == "2":
        print("Correct! 3/10!")
    else:
        livesRemaining -= 1
        print("Incorrect!")
        lifeCount()
    
    print("Question 4: \n 1. Thomas Jefferson \n 2. James K. Polk \n 3.John Adams")
    response = input()
    if response == "3":
        print("Correct! 4/10!")
    else:
        livesRemaining -= 1
        print("Incorrect!")
        lifeCount()
    
    print("Question 5: \n 1. Ulysses S. Grant  \n 2. William Henry Harrison  \n 3. Franklin Pierce")
    response = input()
    if response == "2":
        print("Correct! 5/10!")
    else:
        livesRemaining -= 1
        print("Incorrect!")
        lifeCount()
    
    print("Question 6:  \n 1.Herbert Hoover  \n 2. Grover Cleveland  \n 3. Rutherford B. Hayes")
    response = input()
    if response == "3":
        print("Correct! 6/10!")
    else:
        print("Incorrect!")
        livesRemaining -= 1
        lifeCount()
    print("Question 7:  \n 1. James A. Garfield  \n 2. Calvin Coolidge  \n 3. Franklin D. Roosevelt")
    response = input()
    if response == "1":
        print("Correct! 7/10!")
    else:
        print("Incorrect!")
        livesRemaining -= 1
        lifeCount()
    print("Question 8:  \n 1. Harry S. Truman \n 2. Dwight D. Eisenhower  \n 3. John F. Kennedy ")
    response = input()
    if response == "1":
        print("Correct! 8/10!")
    else:
        print("Incorrect!")    
        livesRemaining -= 1
        lifeCount()
    print("Question 9:  \n 1. Ronald Reagan  \n 2. Richard Nixon  \n 3. Jimmy Carter")
    response = input()
    if response == "2":
        print("Correct! 9/10!")
    else:
        print("Incorrect!")
        livesRemaining -= 1
        lifeCount()
    print("Question 10:  \n 1.George H. W. Bush   \n 2.George W. Bush  \n 3. Bill Clinton")
    response = input()
    if response == "1":
        print("Correct! 10/10!")
    else:
        print("Incorrect!")
        livesRemaining -= 1
        lifeCount()
    
    print("Congrats you win! You got all 10/10 questions right! \nWould you like to play again? Yes or No?")
    response= input()
    if response == "No":
        quit()
