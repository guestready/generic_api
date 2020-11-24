class GenericErrorsHandler:
    def __init__(self, *args, **kwargs):
        pass

    def validate(self, response):
        raise NotImplementedError
