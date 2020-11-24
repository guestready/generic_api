class GenericSession:
    base_url = None

    def __init__(self, *args, **kwargs):
        pass

    def headers(self):
        return {}

    def params(self):
        return {}

    def get_base_url(self):
        assert self.base_url is not None, (
            "'%s' should either include a `base_url` attribute, "
            "or override the `get_base_url()` method."
            % self.__class__.__name__
        )

        return self.base_url
