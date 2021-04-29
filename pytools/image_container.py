import os
import sys
import io 


class ImageHandler:
    _file_path = None
    def __init__(self, file_path = None):
        self._file_path = file_path
    
    def get_image_from_path(self):
        if self._file_path is None:
            raise Exception("No image given as input!")
        with io.open(self._file_path, 'rb') as image_file:
            content = image_file.read()
        return content
    
    def get_image_from_request(self, request_obj):
        return request_obj.files['file'].read()

    def get_image_path(self):
        return self._file_path

    def set_image_path(self, file_path):
        if not os.path.exists(file_path):
            raise Exception("File path does not exist!")
        self._file_path = file_path

