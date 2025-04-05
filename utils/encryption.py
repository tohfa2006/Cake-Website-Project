"""
    By Kevin Caplescu
    Encryption / Datasecurity module used in conjunction with database.
"""
import cryptography.fernet
import os
import dotenv

from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()
raw_key = str.encode(os.getenv("FERNET_KEY"))
key = Fernet(raw_key)

def encrypt(piece_of_data):
    try:
        if type(piece_of_data) == str:
            piece_of_data = str.encode(piece_of_data)
        elif type(piece_of_data) == int:
            piece_of_data = piece_of_data.to_bytes()
        else:
            raise Exception("Invalid data type given.")

        return( key.encrypt(piece_of_data) )
    except:
        return( None )
    
    
def decrypt(piece_of_data):
    try:
        return( key.decrypt(piece_of_data) )
    except:
        return( None )