
# Importing required libraries
from cryptography.fernet import Fernet

# Generate and save a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('encryption_key.key', 'wb') as f:
        f.write(key)

# Load the encryption key
def load_key():
    return open('encryption_key.key', 'rb').read()

# Initialize encryption key
generate_key()
key = load_key()

# Initialize Fernet
cipher_suite = Fernet(key)

# Basic Firewall function
def basic_firewall(ip_address):
    # Simple IP address blocking logic (for demonstration)
    blocked_ips = ['192.168.0.1', '10.0.0.1']
    if ip_address in blocked_ips:
        print(f"Blocked IP address: {ip_address}")
        return False
    else:
        print(f"Allowed IP address: {ip_address}")
        return True

# Password Management function
def manage_password(service, password):
    # Encrypt the password
    encrypted_password = cipher_suite.encrypt(password.encode())
    
    # Store the encrypted password (in a real system, this should be stored in a secure database)
    with open(f'{service}_password.enc', 'wb') as f:
        f.write(encrypted_password)

# Function to retrieve a password
def retrieve_password(service):
    try:
        with open(f'{service}_password.enc', 'rb') as f:
            encrypted_password = f.read()
            
        # Decrypt the password
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password
    except FileNotFoundError:
        print(f"No password found for {service}")
        return None
