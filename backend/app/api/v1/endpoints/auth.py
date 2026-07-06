from fastapi import APIRouter

router = APIRouter()


# Authentication (login, refresh, logout)

@router.get("/")
def list_auth():
    return {"message": "auth endpoint placeholder"}
