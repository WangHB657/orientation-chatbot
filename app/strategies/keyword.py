import re
from .base import MatchingStrategy

class KeywordMatchStrategy(MatchingStrategy):
    def match(self, query: str, faq_data: list) -> str:
        query_words = set(re.findall(r'\w+', query.lower()))
        best_match = max(
            faq_data,
            key=lambda item: len(query_words & set(re.findall(r'\w+', item["question"].lower()))) /
                             len(query_words | set(re.findall(r'\w+', item["question"].lower()))),
            default=None
        )
        if best_match:
            score = len(query_words & set(re.findall(r'\w+', best_match["question"].lower()))) / \
                    len(query_words | set(re.findall(r'\w+', best_match["question"].lower())))
            if score > 0.4:
                return best_match["answer"]
        return ""
