class ScoringService:
    """Business logic for computing farm suitability / credit scores."""

    def compute_score(self, farm_data: dict) -> float:
        raise NotImplementedError
