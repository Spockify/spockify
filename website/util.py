from flask import Response
from bson import json_util

def json_response(data):
    return Response(response=json_util.dumps(data),
        status=200, mimetype='application/json')
