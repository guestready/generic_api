from datetime import timedelta

from constance import config
from django.utils import timezone

from .generics import GenericSession


class ConstanceSession(GenericSession):
    constance_key = None

    def headers(self):
        return {}

    def params(self):
        return {'access_token': getattr(config, self.constance_key)}


class OAuthSession(GenericSession):
    token_name = 'Bearer'
    token_class = None
    refresh_token_function = None

    def __init__(self, *args, **kwargs):
        self.token = self.get_token()
        super().__init__(*args, **kwargs)

    def get_token_class(self, *args, **kwargs):
        assert self.token_class is not None, (
            "'%s' should either include a `token_class` attribute, "
            "or override the `get_token_class()` method."
            % self.__class__.__name__
        )

        return self.token_class

    def get_token_name(self, *args, **kwargs):
        assert self.token_name is not None, (
            "'%s' should either include a `token_name` attribute, "
            "or override the `get_token_name()` method."
            % self.__class__.__name__
        )

        return self.token_name

    def get_refresh_token_function(self):
        assert self.refresh_token_function is not None, (
            "'%s' should either include a `refresh_token_function` attribute, "
            "or override the `get_refresh_token_function()` method."
            % self.__class__.__name__
        )

        return self.refresh_token_function

    def get_access_token(self):
        if not self.token.access_token or (
            self.token.access_token and timezone.now() >= self.token.expiry - timedelta(minutes=10)
        ):
            self.token = self.get_refresh_token_function()(token=self.token, base_url=self.get_base_url())

        return self.token.access_token

    def get_token(self, *args, **kwargs):
        try:
            return self.token
        except AttributeError:
            token_class = self.get_token_class()
            return token_class.objects.first(*args, **kwargs)

    def headers(self):
        return {'Authorization': f'{self.get_token_name()} {self.get_access_token()}'}
