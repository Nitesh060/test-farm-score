from fastapi import APIRouter

router = APIRouter()


# Credit / suitability scoring endpoints

@router.get("/")
def list_scoring():
    return {"message": "scoring endpoint placeholder"}
