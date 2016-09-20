class TokenFetcher:
    shared_state = {}
    tokens_fetched = False

    def __init__(self, unittest=None):
        self.__dict__ = self.shared_state
        if not TokenFetcher.tokens_fetched:
            if unittest is not None:
                self.shared_state = unittest
            else:
                pass
            self.tokens_fetched = True

    def get_tokens(self, key):
        return self.shared_state.get(key, None)
