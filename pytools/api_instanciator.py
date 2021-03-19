import os
from google.cloud import vision
import pytools.image_container as container
#Creates a container class for the handling of the cloud vision API


class CloudAPI:
    _client = None
    _image_parser = None
    def __init__(self, *args, **kwargs):
        self._client = vision.ImageAnnotatorClient()
        self._image_parser = vision.Image 

    def parse_image(self, image_path):
        content = self._handle_image_binary(image_path)

        image = self._image_parser(content=content)

        response = self._client.text_detection(image=image)

        return self._decorate_json_file(response)

    def _handle_image_binary(self, image_path):
        handler = container.ImageHandler(image_path)

        bin_file = handler.get_image_content()

        return bin_file

    def _decorate_json_file(self, response):
        result = []
        for text in response.text_annotations:
            result.append(str(text.description))
        return result



