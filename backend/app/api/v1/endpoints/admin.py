from fastapi import APIRouter

router = APIRouter()


# Admin-only management endpoints

@router.get("/")
def list_admin():
    return {"message": "admin endpoint placeholder"}
