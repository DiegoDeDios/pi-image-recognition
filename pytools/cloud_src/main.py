# Imports the Google Cloud client library
from google.cloud import vision
from flask import escape, jsonify, request
from cloud_vision_handler import CloudAPI
from base_64_hanlder import Base64ImageHandler
import base64

def parse_request_image(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    encoding_handler = Base64ImageHandler()
    text_detector = CloudAPI()
    try:
        #base64_image = request_json['image']
        #content = encoding_handler.decode_from_base64(base64_image)
        content = request.files['file'].read()
        out, error, override = text_detector.detect_text(content)
        return {"counter_text":out, "_error_probability": "{:.2%}".format(error), "_overriden_string": override }
    except Exception as e:
        return jsonify(str(e))