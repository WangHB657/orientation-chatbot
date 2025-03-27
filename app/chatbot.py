from strategies.base import MatchingStrategy


class Chatbot:
    def __init__(self, strategy: MatchingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: MatchingStrategy):
        self.strategy = strategy

    def get_response(self, query: str, faq_data: list) -> str:
        return self.strategy.match(query, faq_data)
