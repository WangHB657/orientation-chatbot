from fuzzywuzzy import process
from .base import MatchingStrategy

class FuzzyMatchStrategy(MatchingStrategy):
    def match(self, query: str, faq_data: list) -> str:
        questions = [item["question"] for item in faq_data]
        best_match = process.extractOne(query, questions)
        if best_match and best_match[1] > 75:
            for item in faq_data:
                if item["question"] == best_match[0]:
                    return item["answer"]
        return ""
