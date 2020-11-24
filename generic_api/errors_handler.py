from .generics import GenericErrorsHandler


class HttpErrorsHandler(GenericErrorsHandler):
    def validate(self, response):
        response.raise_for_status()
        return response.json()
