from fastapi import FastAPI
from app.routers import users, crop_doctor
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title="KisanOne Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

#include the routers
app.include_router(users.router)
app.include_router(crop_doctor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to KisanOne Backend"}

handler = app