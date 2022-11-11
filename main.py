from Encrypt import Encrypt
from Decrypt import Decrypt
import random

shift_pattern = random.randint(1, 26) # Just generate a random int between 1 - 26.
string_to_encrypt = "Version Control System is fun"

encrypted_message = Encrypt(shift_pattern, string_to_encrypt)
decrypted_message = Decrypt(shift_pattern, encrypted_message.result)

print(f"Shift Pattern: {str(shift_pattern)}")
print(f"Encrypted Message: {encrypted_message.result}")

print(f"Decrypted Message: {decrypted_message.result}")


