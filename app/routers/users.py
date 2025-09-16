from fastapi import APIRouter, Depends
from app.core.auth import verify_firebase_token
from app.core.config import supabase

# User router
router = APIRouter()

# Sync user data with Supabase
@router.post("/sync")
def sync_user(user=Depends(verify_firebase_token)):
    uid = user["uid"]
    phone = user.get("phone_number")

    supabase.table("users").upsert({
        "id": uid,
        "phone": phone
    }).execute()