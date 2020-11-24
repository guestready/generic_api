class GenericEndpoint:
    endpoint_url = None
    client_class = None

    def get_endpoint_url(self, *args, **kwargs):
        assert self.endpoint_url is not None, (
            "'%s' should either include a `endpoint_url` attribute, "
            "or override the `get_endpoint_url()` method."
            % self.__class__.__name__
        )
        return self.endpoint_url.format(*args)

    def get_client_class(self, *args, **kwargs):
        assert self.client_class is not None, (
            "'%s' should either include a `client_class` attribute, "
            "or override the `get_session_class()` method."
            % self.__class__.__name__
        )

        return self.client_class

    def get_client_context(self, *args, **kwargs):
        return {}

    def get_client(self, *args, **kwargs):
        """
        Return instantiated client
        """
        client_class = self.get_client_class()
        kwargs['context'] = self.get_client_context()
        return client_class(*args, **kwargs)
