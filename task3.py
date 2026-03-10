import random
import string

def generate_password(length, level):
    if level == "weak":
        characters = string.digits
    elif level == "medium":
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif level == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None  
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    length_pw = int(input("Enter the length of the password: "))
    level_pw = input("How strong? (weak/medium/strong): ").lower().strip()

    password = generate_password(length_pw, level_pw)
    if password:
        print("Generated Password:",password)
    else:
        print("Invalid strength level!")
    again = input("Generate another? (y/n): ").lower().strip()
    if again != 'y':
        break
print("Done!")
