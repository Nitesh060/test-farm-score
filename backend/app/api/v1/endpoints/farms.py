from fastapi import APIRouter

router = APIRouter()


# Farm record CRUD

@router.get("/")
def list_farms():
    return {"message": "farms endpoint placeholder"}
