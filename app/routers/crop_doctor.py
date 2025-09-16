from fastapi import APIRouter, Depends, UploadFile, File
from app.core.auth import verify_firebase_token
from app.models.crop_report import Report
import os
import tempfile
from app.services.aiservice import generate_report

router = APIRouter(
    prefix="/crop-doctor",
    tags=["Crop Doctor"],
    dependencies=[Depends(verify_firebase_token)],
)

@router.post("/analyze", response_model=Report)
async def report(image: UploadFile = File(...)):
    try:
        if image:
            # Create temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(image.filename)[1]) as temp_file:
                temp_file.write(await image.read())
                image_path = temp_file.name

        # Process the image and generate a report
        result = generate_report(image_path)

        # Clean up the temporary file
        os.remove(image_path)

        return result
    
    except Exception as e:
        return {"error": str(e)}