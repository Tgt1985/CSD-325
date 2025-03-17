# Sean Dudley
# CSD-325 - Advanced Python : Module 1.3 Assignment
# 3/12/2025, 3/15, 3/16



# Constant to control the loop
stop = 0

# Create a funciton to run bottle_song
def bottle_song(bottle):

    # Use while loop so that bottle will update as the loop progresses
    while bottle > 0:

        next_btl = (bottle - 1)


        if bottle > 1:
            print(f'{bottle} bottles of beer on the wall, {bottle} bottles of beer. Take one down and pass it around, you have {next_btl} bottles of beer left on the wall.')
        
        # Changed the output to show that there was only 1 bottle of beer
        elif bottle == 1:
            print(f'{bottle} bottle of beer on the wall, {bottle} bottle of beer. Take one down and pass it around, you have {next_btl} bottles of beer left on the wall.')

        # Inform the user they will need to make a purchase before playing again
        if next_btl == 0:
            print('Please purchase more beer to continue playing!')     

        bottle -= 1   
    
# Create a second function that will collect the user data that we will feed into bottle_song
def user_bottles():

    # Return this, do not print. This return will be used to create a constant
    return int(input('How many bottles of beer are you starting with?: '))
    

# Call the main function

if __name__ == '__main__':

    # Use a while loop to allow the loop to be initiated when the user enters 0. This will also take care of any negative numbers and will create a seperate print out keeping both functions seperate

    while True:

        bottle = user_bottles() 
        
        if bottle < 0:
            print('I am sorry, you are unable to have less than Zero bottles.')
            
        bottle_song(bottle)    

        # Initiate the loop to stop if user enters 0
        stop = int(input('Would you like to replay this song? (Please press 1 to play again or 0 to end):'))
        if stop == 0:
            print('You have chosen to stop the song.')
            break
