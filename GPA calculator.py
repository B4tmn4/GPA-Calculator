def main():
    unit_credit_points = 12


    while True:
        try:
            num_of_units = int(input("How many units are there?: "))
            if num_of_units <= 0:
                raise ValueError("Number of units must be a positive integer.")

            # Initialize counts for each grade type
            HD_count = 0
            D_count = 0
            CR_count = 0
            P_count = 0
            F_count = 0

            # Input process for HD
            while True:
                try:
                    HD_count = int(input("How many HD's did you get?: "))
                    if HD_count < 0:
                        raise ValueError("Number of HD's must be non-negative.")
                    break  # Exit the loop if input is successful
                except ValueError as e:
                    print("Error:", e)
                    pass

            # Input process for D
            while True:
                try:
                    D_count = int(input("How many distinctions did you get?: "))
                    if D_count < 0:
                        raise ValueError("Number of distinctions must be non-negative.")
                    break  # Exit the loop if input is successful
                except ValueError as e:
                    print("Error:", e)
                    pass

            # Input process for CR
            while True:
                try:
                    CR_count = int(input("How many credits did you get?: "))
                    if CR_count < 0:
                        raise ValueError("Number of credits must be non-negative.")
                    break  # Exit the loop if input is successful
                except ValueError as e:
                    print("Error:", e)
                    pass

            # Input process for P
            while True:
                try:
                    P_count = int(input("How many passes did you get?: "))
                    if P_count < 0:
                        raise ValueError("Number of passes must be non-negative.")
                    break  # Exit the loop if input is successful
                except ValueError as e:
                    print("Error:", e)
                    pass

            # Input process for F
            while True:
                try:
                    F_count = int(input("How many fails did you get?: "))
                    if F_count < 0:
                        raise ValueError("Number of fails must be non-negative.")
                    break  # Exit the loop if input is successful
                except ValueError as e:
                    print("Error:", e)
                    pass

            # Calculate the sum of units provided by the user
            total_units_provided = HD_count + D_count + CR_count + P_count + F_count

            # Check if the total units provided match the number of units entered
            if total_units_provided != num_of_units:
                raise ValueError(f"The sum of units entered: {num_of_units} , does not match the total number of units provided: {total_units_provided}.")

            # Calculate GPA
            total_grade_points = HD_count * 48 + D_count * 36 + CR_count * 24 + P_count * 12
            GPA = round(total_grade_points / (unit_credit_points * num_of_units), 1)

            print("\nCongratulations! You have a GPA of:", GPA)

        except ValueError as e:
            print("Error:", e)
            # If there's an error, the program will return to the start, allowing the user to input the number of units again

        # Ask the user if they want to calculate another GPA
        calculate_another = input("\nDo you want to calculate another GPA? (yes/no): ").lower()
        if calculate_another != "yes":
            print("\nThank you for using the GPA calculator. Goodbye!")
            break
if __name__ == "__main__":
    main()

# Keep the terminal window open until the user presses Enter
input("\nPress Enter to exit...")


