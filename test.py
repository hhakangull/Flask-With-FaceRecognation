import binascii
import hashlib
import os


def hash_pass(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return salt + pwdhash  # return bytes


def verify_pass(provided_password, stored_password):
    """Verify a stored password against one provided by user"""
    stored_password = stored_password.decode('ascii')
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


first = hash_pass("Hakan")
hakan = "9d97237a473d5c923c97411b67002973b103effbaef44cba8fa591596af9b1fd7969a4e26dd29fc852ed492986314d2bc9a935c41861801aa6498ac49d6503f02d21b574ae801c6b58e51facb0345a0a55e9c67866204511fae5b8918bb509b0"
print(first)
x = verify_pass("Hakan", hakan.encode('utf-8'))

print(x)
