import uuid 
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generate_24_char_string_id():
    uuid_hex = uuid.uuid4().hex
    return uuid_hex[0:24]

def generate_uuid_v4():
    uuid_v4 = uuid.uuid4()
    return uuid_v4