from typing import Union
import bcrypt


class CryptUtils:
    @classmethod
    def encrypt_password(cls, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @classmethod
    def compare_password(cls, password: str, encrypted: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            encrypted.encode("utf-8"),
        )
