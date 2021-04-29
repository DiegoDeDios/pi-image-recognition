import os
from google.cloud import vision
import pytools.image_container as container
#Creates a container class for the handling of the cloud vision API


class CloudAPI:

    _client = None
    _image_parser = None
    COUNTER_LEN = 6 #Every counter should be exactly 6 digits

    def __init__(self, *args, **kwargs):
        self._client = vision.ImageAnnotatorClient()
        self._image_parser = vision.Image 

    def parse_image_from_request(self, request_obj):
        if not request_obj.files["file"]:
            raise Exception("Empty request")

        content = self._handle_image_binary_from_request(request_obj)

        image = self._image_parser(content=content)

        response = self._client.text_detection(image=image)

        return self._decorate_json_file(response)

    def _handle_image_binary_from_request(self, request_obj):
        handler = container.ImageHandler()

        bin_file = handler.get_image_from_request(request_obj)
        return bin_file

    def _handle_image_binary(self, image_path):
        handler = container.ImageHandler(image_path)

        bin_file = handler.get_image_from_path()

        return bin_file

    def _analyze_response_data(self, response):
        decorated_info = []
        replaced_counter = 0
        error_margin = 0.0
        string_override = False 
        if len(response)!=2:
            raise Exception("Image Response not valid")
        for data in response:
            error_margin += 1.0 - len(data)/self.COUNTER_LEN if len(data) < 6 else 0.0
            if not data.isnumeric():
                print("Letter found in string!, original string was: %s"%(data))
                string_override= True
                for character in data:
                    if character == "I":
                        data = data.replace(character,"1")
                        replaced_counter+=1
                    elif character == "o" or character == "O":
                        replaced_counter+=1
                        data = data.replace(character, "0")
                    elif character == "E":
                        replaced_counter+=1
                        data = data.replace(character,"3")
                decorated_info.append(data)
            else:
                decorated_info.append(data)
        error_margin += replaced_counter/self.COUNTER_LEN
        return decorated_info, error_margin, string_override

    def _decorate_json_file(self, response):
        result = []
        for text in response.text_annotations:
            result.append(str(text.description))
        decorated_result, error_percentage, string_override = self._analyze_response_data(result[1:])
        return decorated_result, error_percentage, string_override




