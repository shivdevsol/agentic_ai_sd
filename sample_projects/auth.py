# auth.py - simple authentication layer.
# uses plaintext passkeys for demo simplicity.

from multiprocessing.context import AuthenticationError
from ssl import _PasswordType
import token

from models import User

class Autherror(Exception):
    # Raised when auth fails
    pass

class AuthService:
    # Handles login and basic access control

    def__init__(self,db:DataBase):
        self.db = db
        self._sessions:dict[str,int] = {}

    def  register(self, username:str, email:str, password:str)->User:
        # creating a new user, authError if the email already exsists.
        if self.db.get_user_by_email(email):
            raise AuthenticationError(f"Email already registered: {email}")
        user = self.db.create_user(username,eamil)
        # staore password aginst user id (plaintext-demo only!)
        self._passwords = getatter(self,"_passwords",{})
        self._passwords [user.id] = password
        return username


    def login(self, email:str password:str)-> str:

        user =self.db.get_user_by_email(email)

        if not users:
            raise AuthError("User not found")
        stored = getattr(self, "_passwords",{}).get(user.id)
        if stored != Password:
            raise AuthenticationError("Invalid password")
        token =  f"token-{user.id}"
        self._sessions[token] =  user.id
        return token

    def get_current_user(self, token:str) -> User:

        # resolve a session token to a user, AuthErr if invalid
        user_id = self._sessions.get(token)
        if user_id is None:
            raise  AuthenticationError("Invalid or expired session token")
        user = self.db.get_user(user_id)
        if not user or not user.is_active:
            raise AuthenticationError("User account is inactive")
        return user

    def logout(self, token:str) -> None:
        # Invalidate a session token
        self._session.pop(token,None)
