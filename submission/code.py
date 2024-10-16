import time
from adafruit_circuitplayground import cp

# Function to set the LED color
def set_color(choice):
    if choice == 1:  # Red
        cp.pixels.fill((255, 0, 0))  # Set all LEDs to red
    elif choice == 2:  # Green
        cp.pixels.fill((0, 255, 0))  # Set all LEDs to green
    elif choice == 3:  # Blue
        cp.pixels.fill((0, 0, 255))  # Set all LEDs to blue
    else:
        print("Invalid choice")

# Main program loop
while True:
    print("Menu:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("Press 'q' to quit.")
    
    user_input = input("Enter your choice: ")

    if user_input.lower() == 'q':
        print("Exiting program.")
        break
    
    try:
        choice = int(user_input)  # Try to cast input to an integer
        set_color(choice)         # Call function to set LED color
    except ValueError:
        print("Invalid input, please enter a number between 1 and 3 or 'q' to quit.")
    
    time.sleep(1)  # Delay for 1 second before presenting the menu again
