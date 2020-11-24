from . import mixins
from .generics import GenericEndpoint


class GetEndpoint(mixins.GetRequestMixin, GenericEndpoint):
    """
    Concrete endpoint to perform get query
    """
    def get(self, *args, **kwargs):
        return self.get_request(*args, **kwargs)


class PostEndpoint(mixins.PostRequestMixin, GenericEndpoint):
    """
    Concrete endpoint to perform post query
    """
    def post(self, *args, **kwargs):
        return self.post_request(*args, **kwargs)
