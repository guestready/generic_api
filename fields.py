from rest_framework.serializers import DecimalField, UUIDField


class RequestUUIDField(UUIDField):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return str(value)


class RequestDecimalField(DecimalField):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return str(value)
