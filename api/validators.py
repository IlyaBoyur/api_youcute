from rest_framework import serializers


class NotEqualFieldsValidator:
    message = 'Field values shall not be equal.'

    def __init__(self, fields, message=None):
        self.fields = fields
        self.message = message or self.message

    def __call__(self, attrs):
        unique_required_fields = set([
            attrs[field]
            for field in attrs
            if field in self.fields
        ])
        if len(self.fields) != len(unique_required_fields):
            raise serializers.ValidationError(self.message)
