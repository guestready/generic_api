import json

import requests


class GenericClient:
    session_class = None
    errors_handler_class = None
    retries_handler_class = None

    def __init__(self, *args, **kwargs):
        pass

    def get_session_class(self, *args, **kwargs):
        assert self.session_class is not None, (
            "'%s' should either include a `session_class` attribute, "
            "or override the `get_session_class()` method."
            % self.__class__.__name__
        )

        return self.session_class

    def get_session_context(self, *args, **kwargs):
        return {}

    def get_session(self, *args, **kwargs):
        """
        Return instantiated session
        """
        session_class = self.get_session_class()
        kwargs['context'] = self.get_session_context()
        return session_class(*args, **kwargs)

    def get_errors_handler_class(self, *args, **kwargs):
        assert self.errors_handler_class is not None, (
            "'%s' should either include a `errors_handler_class` attribute, "
            "or override the `get_errors_handler_class()` method."
            % self.__class__.__name__
        )

        return self.errors_handler_class

    def get_errors_handler_context(self, *args, **kwargs):
        return {}

    def get_errors_handler(self, *args, **kwargs):
        errors_handler_class = self.get_errors_handler_class()
        kwargs['context'] = self.get_errors_handler_context()
        return errors_handler_class(*args, **kwargs)

    def get_retries_handler_class(self, *args, **kwargs):
        return self.retries_handler_class

    def get_retries_handler_context(self, *args, **kwargs):
        return {}

    def get_retries_handler(self, *args, **kwargs):
        retries_handler_class = self.get_retries_handler_class()

        if retries_handler_class:
            kwargs['context'] = self.get_retries_handler_context()
            return retries_handler_class(*args, **kwargs)
        else:
            return None

    def get_base_url(self):
        return self.get_session().get_base_url()

    def _request(self, http_method, endpoint_url, data=None, params={}, retries_handler=None):
        session = self.get_session()
        retries_handler = retries_handler or self.get_retries_handler()
        error_handler = self.get_errors_handler()
        request_headers = session.headers()
        request_params = {**params, **session.params()}

        response = http_method(
            endpoint_url,
            params=request_params,
            headers=request_headers,
            data=json.dumps(data) if data else None
        )

        if retries_handler and retries_handler.is_eligible(response):
            retries_handler.increment()
            return self._request(http_method, endpoint_url, data, params, retries_handler)

        return error_handler.validate(response)

    def get(self, endpoint_url, *args, **kwargs):
        return self._request(requests.get, endpoint_url, *args, **kwargs)

    def post(self, endpoint_url, data, *args, **kwargs):
        return self._request(requests.post, endpoint_url, data=data, *args, **kwargs)
