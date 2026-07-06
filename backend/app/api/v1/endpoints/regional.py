from fastapi import APIRouter

router = APIRouter()


# Regional aggregates and benchmarks

@router.get("/")
def list_regional():
    return {"message": "regional endpoint placeholder"}
