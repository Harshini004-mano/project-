def pin():
      print("***WELCOME TO PYGAME***")
      print("***Login Credentials***")
      User_id=input("Enter your Userid:")
      correct_pin ="1234"
      while True:
        pin= input("Enter the pin:")
        if pin== correct_pin:
            print("Valid pin")
            break
        elif attempts>= 2:
            print("invalid pin")
            print("Maximum attempts... Access denied...")
        else:
            print("Thank you visit again")
            break
def game():
      pin()
      import random
      secret_number = random.randint(1,20)
      print("***Number Guess***")
      atp=[]
      for atp in range(5):  
            guess = int(input("Take a guess: ",))
            if guess < secret_number:
                print("The guess is low... higher number... Try again.")
            elif guess > secret_number:
                print("The guess is higher... lower number...Try again.")
            else:
                print(f"Congratulations! You guessed it right. The number was {secret_number}.")
                break   
game()
print("Too many attempts try again later")