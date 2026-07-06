from fastapi import APIRouter

router = APIRouter()


# Report generation (PDF/DOCX) endpoints

@router.get("/")
def list_reports():
    return {"message": "reports endpoint placeholder"}
