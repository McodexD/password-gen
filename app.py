import random
import string

def generate_password(length=12, use_special_chars=True, exclude_chars=""):
    """Generate a random password with specified constraints.
    
    Args:
        length (int): The length of the password. Default is 12.
        use_special_chars (bool): Whether to include special characters. Default is True.
        exclude_chars (str): Characters to exclude from the password. Default is "".
        
    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    # Define character pools
    upper_chars = ''.join(set(string.ascii_uppercase) - set(exclude_chars))
    lower_chars = ''.join(set(string.ascii_lowercase) - set(exclude_chars))
    digits = ''.join(set(string.digits) - set(exclude_chars))
    special_chars = ''.join(set(string.punctuation) - set(exclude_chars))
    
    if use_special_chars:
        all_chars = upper_chars + lower_chars + digits + special_chars
    else:
        all_chars = upper_chars + lower_chars + digits
    
    if not all_chars:
        raise ValueError("Character pools are empty after excluding specified characters.")
    
    # Ensure at least one of each required type is included
    password_chars = [
        random.choice(upper_chars),
        random.choice(lower_chars),
        random.choice(digits),
    ]
    if use_special_chars:
        password_chars.append(random.choice(special_chars))
    
    # Fill the rest of the password length with random choices
    password_chars += [random.choice(all_chars) for _ in range(length - len(password_chars))]
    
    # Shuffle the result to ensure randomness
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        exclude_chars = input("Enter characters to exclude (optional): ").strip()
        
        password = generate_password(length, use_special_chars, exclude_chars)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
