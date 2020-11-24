===========
Generic API
===========

Polls is a Django app to reach external APIs by mirroring DRF architecture.

Quick start
-----------

1. Add "generic_api" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'generic_api',
    ]

2. Create your session class that will hold the authentication and the base URL:

    from generic_api.session import ConstanceSession


    class MySession(ConstanceSession):
        base_url = 'https://baseurl/v1/'
        constance_key = 'MY_TOKEN'

3. Create the client that will perform the queries:

    from generic_api.errors_handler import HttpErrorsHandler
    from generic_api.generics import GenericClient


    class MyClient(GenericClient):
        session_class = MySession
        errors_handler_class = HttpErrorsHandler

4. Create the serializers for requests and responses:

    class MyRequestSerializer(serializers.Serializer):
        name = serializers.CharField()

    class MyResponseSerializer(serializers.Serializer):
        id = serializer.IntegerField()

Those are used to valid the request performed and the response received. If allows to detect quickly if something
changed on the remote API

5. Create your endpoint:

    from generic_api.endpoints import GetEndpoint

    class MyEndpointEndpoint(GetEndpoint):
        endpoint_url = 'search/by_name'  # This can take argument, like endpoint_url: '{}/list'
        client_class = MyClient
        response_entity_class = MyResponseSerializer
        request_entity_class = MyRequestSerializer

If your serializer are ModelSerializer, the object can be saved.

6. Use the endpoint:

       endpoint = MyEndpoint()

        data = endpoint.get(\*\*kwargs)
        data = data.save()


This project is available on GitHub: https://github.com/guestready/generic_api