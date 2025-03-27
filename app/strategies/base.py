from abc import ABC, abstractmethod

class MatchingStrategy(ABC):
    @abstractmethod
    def match(self, query: str, faq_data: list) -> str:
        pass
