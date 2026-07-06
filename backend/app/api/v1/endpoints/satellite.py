from fastapi import APIRouter

router = APIRouter()


# Satellite imagery + NDVI retrieval

@router.get("/")
def list_satellite():
    return {"message": "satellite endpoint placeholder"}
