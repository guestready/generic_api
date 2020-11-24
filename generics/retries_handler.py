class GenericRetriesHandler:
    def __init__(self, *args, **kwargs):
        self.count = 0

    def is_eligible(self, response):
        raise NotImplementedError

    def increment(self):
        self.count += 1
