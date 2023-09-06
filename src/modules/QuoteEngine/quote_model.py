class QuoteModel:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        return f"QuoteModel(body={self.body}, author={self.author})"
