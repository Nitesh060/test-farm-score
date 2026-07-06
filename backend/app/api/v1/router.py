from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    farmers,
    farms,
    boundaries,
    satellite,
    regional,
    scoring,
    reports,
    admin,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(farmers.router, prefix="/farmers", tags=["farmers"])
api_router.include_router(farms.router, prefix="/farms", tags=["farms"])
api_router.include_router(boundaries.router, prefix="/boundaries", tags=["boundaries"])
api_router.include_router(satellite.router, prefix="/satellite", tags=["satellite"])
api_router.include_router(regional.router, prefix="/regional", tags=["regional"])
api_router.include_router(scoring.router, prefix="/scoring", tags=["scoring"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
