from urllib.parse import urljoin


class RequestValidationMixin:
    """
    Validate the request sent to the API using an Entity class (mostlikly a Serializer)
    """
    request_entity_class = None

    def get_request_entity_class(self, *args, **kwargs):
        return self.request_entity_class

    def get_request_entity_context(self, *args, **kwargs):
        return {}

    def get_request_entity(self, *args, **kwargs):
        """
        Return instantiated request entity
        """
        request_entity_class = self.get_request_entity_class()

        if request_entity_class:
            kwargs['context'] = self.get_request_entity_context()
            return request_entity_class(*args, **kwargs)
        else:
            return None

    def validate_request(self, data):
        if data is not None:
            request_entity = self.get_request_entity(data=data)

            if request_entity:
                if request_entity.is_valid():
                    return request_entity.validated_data
                else:
                    raise ValueError(request_entity.errors)

        return data


class ResponseValidationMixin:
    """
    Validate the response return by the API using an entity
    """
    response_entity_class = None

    def get_response_entity_class(self, *args, **kwargs):
        return self.response_entity_class

    def get_response_entity_context(self, *args, **kwargs):
        return {}

    def get_response_entity(self, *args, **kwargs):
        """
        Return instantiated response entity
        """
        response_entity_class = self.get_response_entity_class()

        if response_entity_class:
            kwargs = {**kwargs, **self.get_response_entity_context()}
            return response_entity_class(*args, **kwargs)
        else:
            return None

    def validate_response(self, data):
        if data is not None:
            response_entity = self.get_response_entity(data=data)
            if response_entity:
                if response_entity.is_valid():
                    return response_entity
                else:
                    raise ValueError(response_entity.errors)

        return data


class GetRequestMixin(RequestValidationMixin, ResponseValidationMixin):
    """
    Get data from remote API
    """

    def get_request(self, *args, **kwargs):
        client = self.get_client()
        endpoint = urljoin(client.get_base_url(), self.get_endpoint_url(*args))
        params = self.validate_request(data=kwargs)
        data = client.get(endpoint, params=params)
        entity = self.validate_response(data=data)
        return entity


class PostRequestMixin(RequestValidationMixin, ResponseValidationMixin):
    """
    Post data to remote API
    """
    def post_request(self, *args, **kwargs):
        client = self.get_client()
        endpoint = urljoin(client.get_base_url(), self.get_endpoint_url())
        request_data = self.validate_request(data=kwargs)
        data = client.post(endpoint, request_data)
        serializer = self.validate_response(data=data)

        return serializer
