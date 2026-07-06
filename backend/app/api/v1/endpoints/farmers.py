from fastapi import APIRouter

router = APIRouter()


# Farmer profile CRUD

@router.get("/")
def list_farmers():
    return {"message": "farmers endpoint placeholder"}
