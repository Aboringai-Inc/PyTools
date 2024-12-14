import uuid
import random
import string

def uuid_generator():
    """Generates a random UUID."""
    return str(uuid.uuid4())

def generate_password(length=12, use_special_chars=True):
    """Generates a secure password."""
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))
