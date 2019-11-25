from django.http import HttpResponse


class MagicMirrorView:

    def get_response_with_status_code(self, statusCode, body):
        response = HttpResponse()
        response.status_code = statusCode
        response.content = body
        return response

    def get_bad_request(self, body):
        return get_response_with_status_code(400, body)
