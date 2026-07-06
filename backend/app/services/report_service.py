class ReportService:
    """Generates PDF/DOCX reports using WeasyPrint templates."""

    def generate_pdf(self, context: dict) -> bytes:
        raise NotImplementedError
