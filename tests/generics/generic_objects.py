from generic_api.endpoints import GetEndpoint, PostEndpoint
from generic_api.generics import (GenericClient, GenericEndpoint,
                                  GenericEntity, GenericErrorsHandler,
                                  GenericRetriesHandler, GenericSession)


class TestSession(GenericSession):
    base_url = 'https://www.example.com/'


class TestErrorsHandler(GenericErrorsHandler):
    def validate(self, response):
        return response.data


class TestRetriesHandler(GenericRetriesHandler):
    def is_eligible(self, response):
        return False


class TestClient(GenericClient):
    session_class = TestSession
    errors_handler_class = TestErrorsHandler
    retries_handler_class = TestRetriesHandler


class TestGenericEndpoint(GenericEndpoint):
    endpoint_url = 'https://www.example_endpoint.com/'
    client_class = TestClient


class TestGetEndpoint(GetEndpoint):
    endpoint_url = 'https://www.example_endpoint.com/'
    client_class = TestClient


class TestPostEndpoint(PostEndpoint):
    endpoint_url = 'https://www.example_endpoint.com/'
    client_class = TestClient


class TestEntity(GenericEntity):
    def is_valid(self):
        return True

    @property
    def data(self):
        return {}
