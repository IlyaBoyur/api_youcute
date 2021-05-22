from rest_framework.exceptions import APIException


class BadRequestAPIException(APIException):
    status_code = 400
    default_detail = 'Request parameters are faulty.'
    default_code = 'bad_request'
