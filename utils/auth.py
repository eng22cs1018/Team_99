import hashlib
import json
from pathlib import Path

USER_DB_PATH = Path("users.json")

def validate_user(username: str, password: str) -> bool:
    """Authenticate user against stored credentials"""
    if not USER_DB_PATH.exists():
        return False
        
    with open(USER_DB_PATH) as f:
        users = json.load(f)
        
    user = users.get(username)
    if user and user["password"] == hash_password(password):
        return True
    return False

def hash_password(password: str) -> str:
    """Secure password hashing"""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username: str, password: str) -> bool:
    """Create new user account"""
    if USER_DB_PATH.exists():
        with open(USER_DB_PATH) as f:
            users = json.load(f)
    else:
        users = {}
        
    if username in users:
        return False
        
    users[username] = {
        "password": hash_password(password),
        "created_at": datetime.datetime.now().isoformat()
    }
    
    with open(USER_DB_PATH, "w") as f:
        json.dump(users, f, indent=2)
        
    return True