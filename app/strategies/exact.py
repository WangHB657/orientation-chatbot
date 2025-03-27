from .base import MatchingStrategy

class ExactMatchStrategy(MatchingStrategy):
    def match(self, query: str, faq_data: list) -> str:
        query_lower = query.strip().lower()
        for item in faq_data:
            if query_lower == item["question"].lower():
                return item["answer"]
        return ""
