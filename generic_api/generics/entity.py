class GenericEntity:
    def __init__(self, *args, **kwargs):
        pass

    def is_valid(self):
        raise NotImplementedError

    @property
    def data(self):
        raise NotImplementedError
