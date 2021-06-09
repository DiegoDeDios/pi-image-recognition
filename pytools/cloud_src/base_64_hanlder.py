import base64


class Base64ImageHandler:
    encoded_string = None
    def __init__(self, encoded_str = None):
        if encoded_str:
            self.encoded_string = encoded_str

    def decode_from_base64(self, base64_image):
        """Returns a image file object from a base64 string"""
        
        base64_bytes = base64_image.encode("ascii")  
        base64_string_bytes = base64.b64decode(base64_bytes)
        content = base64.b64decode(base64_image)

        return content

    def set_encoded_string(self, encoded_str):
        self.set_encoded_string = encoded_str
