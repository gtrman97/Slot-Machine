# Program Slot Machine 
# Description: 
# 	This program simulates a slot machine. 
# Author: Andrew Killian 
# Date: 11/07/17
# Revised: 
# 	12/16/17 

# list libraries used
import turtle 
import random

slot = turtle.Turtle()

slot.speed(0)

# Declare global constants

# Main Program
def main():

    # Declare variables
    number = 0
    slot1 = 0
    slot2 = 0
    slot3 = 0
    slotList = [] 
    winnings = 0
    total_winnings = 0.0
    play = ''

# Function draw_machines
# Description:
#	Creates a visual representation
#       of three different slot machines
#       using turtle graphics. 
# Calls:
#	none
# Parameters:
#	none
# Returns:
#	none
    
def draw_machines():

    slot.color("blue")

    slot.penup()
    slot.setposition(-325, 300)
    slot.pendown()

    slot.begin_fill()
    slot.forward(200)
    slot.right(90)
    slot.forward(650)
    slot.right(90)
    slot.forward(200)
    slot.right(90)
    slot.forward(650)
    slot.end_fill()
    slot.penup()

    slot.color("blue")

    slot.setposition(-100, 300)
    slot.pendown()

    slot.right(90)
    slot.begin_fill()
    slot.forward(200)
    slot.right(90)
    slot.forward(650)
    slot.right(90)
    slot.forward(200)
    slot.right(90)
    slot.forward(650)
    slot.end_fill()
    slot.penup()

    slot.color("blue")

    slot.setposition(125, 300)
    slot.pendown()

    slot.right(90)
    slot.begin_fill()
    slot.forward(200)
    slot.right(90)
    slot.forward(650)
    slot.right(90)
    slot.forward(200)
    slot.right(90)
    slot.forward(650)
    slot.end_fill()
    slot.penup()

# End Function # draw_machines

# Function draw_screens
# Description:
#	Creates a visual representation
#       of three different slot screens
#       to display the game numbers
#       using turtle graphics. 
# Calls:
#	none
# Parameters:
#	none
# Returns:
#	none

def draw_screens():

    slot.color("white")

    slot.setposition(-300, 275)
    slot.pendown()
    slot.begin_fill()

    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.end_fill()
    slot.penup()

    slot.color("white")

    slot.setposition(-75, 275)
    slot.pendown()
    slot.begin_fill()

    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    
    slot.right(90)
    slot.forward(150)
    slot.end_fill()
    slot.penup()

    slot.color("white")

    slot.setposition(150, 275)
    slot.pendown()
    slot.begin_fill()

    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.right(90)
    slot.forward(150)
    slot.end_fill()
    slot.penup()

# End Function # draw_screens

# Function chance
# Description:
#       This function creates a
#       formula to determine
#       how likely a slot number
#       will spit out a winning number. 
# Calls:
#	none
# Parameters:
#	none
# Returns:
#	number


def chance():

    # Declare local variables
    number = 0
    possibility = 0

    # Generate a random integer between 1 and 100
    possibility = random.randint(1, 100)

    # Determine the slot number based on the random number; if it is
    #  a multiple of 51, the number 100 appears on the screen    (the random number % 51 is 0)
    #  a multiple of 47, the number 75 appears on the screen
    #  a multiple of 23, the number 50 appears on the screen
    #  a multiple of 11, the number 25 appears on the screen
    # Everything else scores nothing
         
    if ( (possibility % 51) == 0 ):
         
        number = 100

         
    elif ( (possibility % 47) == 0 ):
         
        number = 75
         
    elif ( (possibility % 23) == 0 ):
         
        number = 50
         
    elif ( (possibility % 11) == 0 ):
         
        number = 25
         
    else:
         
        number = random.randint(1, 100)
         
    # End If

    # Return values
    return number

# End Function # chance

# Function certificate
# Description:
#	Writes a winner certificate to a text file for you to print.
#       In addition, it prints the numbers that you got on each slot
#       and finally the winning, number that you landed on. 
# Calls:
#	none
# Parameters:
#	none
# Returns:
#	none

def certificate(): 

    # Declare local variables
    outfile = ""

    outfile = open("Winner.txt", 'w')

    outfile.write("Congratulations!" + '\n' "You are the grand prize winner of"
                  + '\n' "Andrew's Amazing Slot Machine Game!" + '\n')

    outfile.write("Please print this and show it to the Quartermaster to claim your prize."
                    + '\n' "Your winning lottery numbers were: "
                  + '\n' "Slot 1: " + str(slotList1) + '\n'
                  "Slot 2: " + str(slotList2) + '\n'
                  "Slot 3: " + str(slotList3))  

    outfile.close

    # Return values

# End Function

draw_machines()
draw_screens() 

# Print the welcome message for the game.
slot.color("blue")
slot.setposition(-250, 350)
slot.pendown()
slot.write('$$$ Welcome to Slot Machine $$$', font=("Arial", 25, "normal"))
slot.penup()

# Prompt the user if they would like to play the game.
print("Welcome to Slot Machine where:") 
print("Number 25 wins $5")
print("Number 50 wins $10")
print("Number 75 wins $15")
print("Number 100 wins $20")
print("And 3 matching numbers wins ???") 
play = input('Would you like to play the game? (y/n) ') 
winnings = 0.0
total = 0.0
slotList = [] 


if play in ['y', 'Y', "Yes", "yes"]: 

    input('Press enter to run slot 1. ')
    again = 'y'

else:
    print("That's a shame, it's a sweet game.")
    again = 'x'

# End If 

while again in ['y', 'Y', "yes", "Yes", "sure", "Sure", "ok", "Ok"]:

    slotList1 = [] 

    for slot1 in range(6):

        slot.color("white")

        slot.setposition(-300, 275)
        slot.pendown()
        slot.begin_fill()

        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.end_fill()
        slot.penup()

        slot.color("blue")

        slot.setposition(-255, 175)
        slot.pendown()
        arg1 = random.randint(1, 100)
        slotList1.append(arg1)
        slot.write(arg1, font=("Arial", 45, "normal"))
        slot.penup()

        if slot1 == 5:
            slot.color("white")

            slot.setposition(-300, 275)
            slot.pendown()
            slot.begin_fill()

            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.end_fill()
            slot.penup()

            slot.color("blue")

            slot.setposition(-255, 175)
            slot.pendown()
            number1 = chance() 
            slot.write(number1, font=("Arial", 45, "normal"))
            slot.penup()
            
            slotList1.append(number1) 
            slotList.append(number1)
                
        # End If 

    # End For 

    input('Press enter to run slot 2.')

    slotList2 = [] 

    for slot2 in range(6):

        slot.color("white")

        slot.setposition(-75, 275)
        slot.pendown()
        slot.begin_fill()

        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.end_fill()
        slot.penup()

        slot.color("blue")

        slot.setposition(-35, 175)
        slot.pendown()
        arg2 = random.randint(1, 100)
        slotList2.append(arg2) 
        slot.write(arg2, font=("Arial", 45, "normal"))
        slot.penup()
        
        if slot2 == 5:
            slot.color("white")

            slot.setposition(-75, 275)
            slot.pendown()
            slot.begin_fill()

            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.end_fill()
            slot.penup()

            slot.color("blue")

            slot.setposition(-35, 175)
            slot.pendown()
            number2 = chance()   
            slot.write(number2, font=("Arial", 45, "normal"))
            slot.penup()

            slotList2.append(number2)
            slotList.append(number2)

        # End If

    # End For

    input('Press enter to run slot 3.')

    slotList3 = [] 

    for slot3 in range(6):

        slot.color("white")

        slot.setposition(150, 275)
        slot.pendown()
        slot.begin_fill()

        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.right(90)
        slot.forward(150)
        slot.end_fill()
        slot.penup()

        slot.color("blue")

        slot.setposition(190, 175)
        slot.pendown()
        arg3 = random.randint(1, 100)
        slotList3.append(arg3) 
        slot.write(arg3, font=("Arial", 45, "normal"))
        slot.penup()
        
        if slot3 == 5:
            slot.color("white")

            slot.setposition(150, 275)
            slot.pendown()
            slot.begin_fill()

            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.right(90)
            slot.forward(150)
            slot.end_fill()
            slot.penup()

            slot.color("blue")

            slot.setposition(190, 175)
            slot.pendown()
            number3 = chance()    
            slot.write(number3, font=("Arial", 45, "normal"))
            slot.penup()
            
            slotList3.append(number3) 
            slotList.append(number3)
                
        # End If

    # End For

            if number1 == 25 and number2 == 25 and number3 == 25:

                print("You won third prize!")
                winnings = 250
                print("You have won $", format(winnings, ',.2f')) 
                again = input("Would you like to play again? ")

            elif number1 == 50 and number2 == 50 and number3 == 50:

                print("You won second prize!")
                winnings = 500
                print("You have won $", format(winnings, ',.2f')) 
                again = input("Would you like to play again? ")

            elif number1 == 75 and number2 == 75 and number3 == 75:

                print("You won first prize!")
                winnings = 750
                print("You have won $", format(winnings, ',.2f')) 
                again = input("Would you like to play again? ")

            elif number1 == 100 and number2 == 100 and number3 == 100:

                print("Grand Prize Winner!")
                winnings = 1000
                print("You have won $", format(winnings, ',.2f')) 
                print("Open 'Winner.txt' to print out your certificate.") 
                certificate()
                turtle.done()
                again = 'n' 

            else:

                total = 0.0

                for item in slotList:

                    if item == 25:
                        winnings = 5
                    elif item == 50:
                        winnings = 10
                    elif item == 75:
                        winnings = 15
                    elif item == 100:
                        winnings = 20
                    else:
                        winnings = 0

                    # Keep a running total of the user's winnings. 
                    total += winnings

                    # End If 
                    
                print("Game Over") 
                print("Your winnings total $", format(total, ',.2f'))
                again = input("Would you like to play again? ")

                # End For 

            # End If

# End While

# End Program
main() 




        
