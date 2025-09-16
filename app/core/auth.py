from fastapi import Header, HTTPException
from firebase_admin import auth

# Verify Firebase ID Token 
def verify_firebase_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        decoded = auth.verify_id_token(token)
        return decoded
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")