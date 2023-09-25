import random
import string

def generate_username(length=8):
    unique_usernames = set()
    
    # Read existing usernames from the file, if any
    try:
        with open('usernames.txt', 'r') as file:
            for line in file:
                username = line.strip()
                unique_usernames.add(username)
    except FileNotFoundError:
        pass

    while True:
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if username not in unique_usernames:
            unique_usernames.add(username)
            yield username

username_generator = generate_username()

while True:
    new_username = next(username_generator)
    print("Generated username:", new_username)
    
    # Open the file in append mode and check for duplicates
    with open('usernames.txt', 'a+') as file:
        file.seek(0)  # Move to the beginning of the file
        if new_username in file.read():
            print("Error: Username already present in the txt file.")
        else:
            # Write the new username to the file
            file.write(new_username + '\n')
    
    input("Press Enter to generate the next username...")
