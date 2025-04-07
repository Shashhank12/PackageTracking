import re # Library for regular expressions (regex) used to search for status related information

# Simulate a database of tracking numbers and their statuses
tracking_numbers_and_status = {
    "1234567890": "Shipped. Expected delivery on 2025-04-10.",
    "0987654321": "Delivered. Delivered on 2025-04-06.",
    "1122334455": "Out for delivery. Expected delivery by 08:00 PM.",
    "5544332211": "Not found."
}

# Stores order numbers and their corresponding tracking numbers
order_tracking_numbers = {
    "111111": "1234567890",
    "222222": "0987654321",
    "333333": "1122334455",
    "444444": "5544332211"
}

# Function that checks if a tracking number is valid
def valid_tracking_number(tracking_number):
    return tracking_number in tracking_numbers_and_status

# Function that takes care of potential customer support contact
def contact_support():
    print("Would you like to contact support?")
    user_input = input("Please enter 'yes' or 'no': ").strip().lower()
    # Loop til a valid response is given
    while user_input not in ["yes", "no"]:
        user_input = input("Please enter 'yes' or 'no': ").strip().lower()
    if user_input == "yes":
        # Provide a temporary support number
        print("Please call 1-800-000-0000")
    else:
        print("Have a great day!")
        
# Function that checks the status of the package based on the tracking number and 
# uses regular expressions to extract relevant information
def check_package_status(tracking_number):
    # Search for the status of the package using the tracking number
    match = re.search(r"^(?P<status>.+?)\.", tracking_numbers_and_status[tracking_number])
    # Take the status from the match object
    # and check if it is one of the expected statuses
    if match:
        status = match.group("status")
        # Handles the cases that the package is shipped
        if status == "Shipped":
            print("Your package has been shipped.")
            # Extract the expected delivery date using regex
            match = re.search(r"Expected delivery on (?P<date>\d{4}-\d{2}-\d{2})", tracking_numbers_and_status[tracking_number])
            if match:
                date = match.group("date")
                print(f"Expected delivery date is {date}.")
        # Handles the delivered case
        elif status == "Delivered":
            print("Your package has been delivered.")
            # Regex to extract the delivery date
            match = re.search(r"Delivered on (?P<date>\d{4}-\d{2}-\d{2})", tracking_numbers_and_status[tracking_number])
            if match:
                # Extract the date from the match object
                # and ask the user if they found the package
                date = match.group("date")
                print(f"Delivered on {date}. Please check your delivery location.")
                print("Did you find it?")
                user_input = input("Please enter 'yes' or 'no': ").strip().lower()
                while user_input not in ["yes", "no"]:
                    user_input = input("Please enter 'yes' or 'no': ").strip().lower()
                if user_input == "yes":
                    print("Thank you!")
                else:
                    # If the package is not found, ask the user to check other locations or contact support. Support can further help with lost, stolen, or misplaced packages.
                    print("Please check other locations or contact support.")
                    contact_support()
        # Handles the case that the package is out for delivery
        elif status == "Out for delivery":
            print("Your package is out for delivery.")
            # Regex to extract the expected delivery time
            match = re.search(r"Expected delivery by (?P<time>\d{1,2}:\d{2} [AP]M)", tracking_numbers_and_status[tracking_number])
            if match:
                # Provides the user with the expected delivery time
                time = match.group("time")
                print(f"Expected delivery time is {time}.")
                print("Thank you")
        else:
            print("Tracking number not found.")
            contact_support()

# Starting of the program
print("I can help track your package. Do you have your tracking number?")
user_input = input("Please enter 'yes' or 'no': ").strip().lower()
# Loop til a valid response is given
while user_input not in ["yes", "no"]:
    user_input = input("Please enter 'yes' or 'no': ").strip().lower()
if user_input == "yes":
    # Prompt the user for their tracking number
    # and check if it is valid
    tracking_number = input("Please enter your 10-digit tracking number: ")
    while len(tracking_number) != 10 or not tracking_number.isdigit():
        tracking_number = input("Invalid tracking number. Please enter a valid 10-digit tracking number: ").strip()
    if valid_tracking_number(tracking_number):
        print("Valid tracking number. Checking your package status.")
        check_package_status(tracking_number)
    else:
        print("Tracking number not found.")
        contact_support()
elif user_input == "no":
    # Allows the user to also enter their order number if they do not have a tracking number
    # Checks to make sure order number is valid and uses that to find the tracking number
    print("Do you have an order number?")
    user_input = input("Please enter 'yes' or 'no': ").strip().lower()
    while user_input not in ["yes", "no"]:
        user_input = input("Please enter 'yes' or 'no': ").strip().lower()
    if user_input == "yes":
        order_number = input("Please enter your 6-digit order number: ")
        while len(order_number) != 6 or not order_number.isdigit():
            order_number = input("Invalid order number. Please enter a valid 6-digit order number: ").strip()
        # Check if the order number is valid and retrieve the tracking number
        if order_number in order_tracking_numbers:
            tracking_number = order_tracking_numbers[order_number]
            print(f"Your tracking number is {tracking_number}.")
            if valid_tracking_number(tracking_number):
                check_package_status(tracking_number)
            else:
                # Provide customer support if the tracking number is not found
                print("Tracking information not found.")
                contact_support()
        else:
            print("Order number not found.")
            contact_support()
    else:
        # If the user does not have a tracking number or order number, provide customer support
        print("Please contact support for further assistance.")
        contact_support()