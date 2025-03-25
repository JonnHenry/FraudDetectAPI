from fastapi import APIRouter
from app.controllers.prediction_controller import router as ml_router

router_  = APIRouter()
router_.include_router(ml_router)