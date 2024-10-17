from adafruit_circuitplayground import cp

def change_led_color(choice):
    """
    This function changes the color of the LEDs based on the user's choice.
    1: Red, 2: Green, 3: Blue
    """
    if choice == 1:
        cp.pixels.fill((255, 0, 0))  # Red color
        print("Red color selected")
    elif choice == 2:
        cp.pixels.fill((0, 255, 0))  # Green color
        print("Green color selected")
    elif choice == 3:
        cp.pixels.fill((0, 0, 255))  # Blue color
        print("Blue color selected")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

while True:
    # Displaying the menu options
    print("\nMenu:")
    print("1. Red Color")
    print("2. Green Color")
    print("3. Blue Color")
    print("Press 'q' to quit.")

    # Getting user input
    user_input = input("Choose a color option: ")

    # Check if the user pressed 'q' to quit the program
    if user_input == 'q':
        print("Exiting the program.")
        break  # Exits the while loop, ending the program

    try:
        # Convert the input to an integer
        choice = int(user_input)

        # Call the function to change LED color based on user's choice
        change_led_color(choice)

    except ValueError:
        # Catch invalid inputs that cannot be converted to an integer
        print("Invalid input. Please enter a number (1, 2, or 3) or 'q' to quit.")

