from fastapi import APIRouter

router = APIRouter()


# Farm boundary / geo-polygon management

@router.get("/")
def list_boundaries():
    return {"message": "boundaries endpoint placeholder"}
