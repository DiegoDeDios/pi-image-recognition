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

    def _analyze_response_data(self, response):
        decorated_info = []
        for data in response:
            if not data.isnumeric():
                print("Letter found in string!, original string was: %s"%(data)) #TODO replace temporal print for logic to reeplace letter for most similar match
                for character in data:
                    if character == "I":
                        data = data.replace(character,"1")
                    elif character == "o" or character == "O":
                        data = data.replace(character, "0")
                    elif character == "E":
                        data = data.replace(character,"3")
                decorated_info.append(data)
            else:
                decorated_info.append(data)
        return decorated_info

    def _decorate_json_file(self, response):
        result = []
        for text in response.text_annotations:
            result.append(str(text.description))
        decorated_result = self._analyze_response_data(result[1:])
        return decorated_result



