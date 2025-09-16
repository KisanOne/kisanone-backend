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
    # Fallback to displayName if name is not available
    name = user.get("name") or user.get("displayName")  

    if not phone:
        raise ValueError("Phone number is required")

    supabase.table("users").upsert({
        "id": uid,
        "phone": phone,
        "name": name
    }).execute()

    return {"status": "success", "id": uid, "phone": phone, "name": name}