from google.cloud import vision


class CloudAPI:
    _client = vision.ImageAnnotatorClient()
    
    def detect_text(self, content):
        image = vision.Image(content=content)

        response = self._client.text_detection(image=image)

        decorated_info, error_margin, string_override = self.decorate_json_file(response)

        return decorated_info, error_margin, string_override

    def analyze_response_data(self, response):
            decorated_info = []
            replaced_counter = 0
            error_margin = 0.0
            string_override = False 
            if len(response)!=2:
                respone_len = len(response)
                if respone_len > 2:
                    # for index in range(2,respone_len-1):
                    #     response.pop(index)
                    response = response[:2]
                else:
                    raise Exception({"message":"Image not clear enough: ","counter_text":response, "_error_probability": "{:.2%}".format(1.0), "_overriden_string": string_override })
            for data in response:
                error_margin += 1.0 - len(data)/6 if len(data) < 6 else 0.0
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
            error_margin += replaced_counter/6
            return decorated_info, error_margin, string_override

    def decorate_json_file(self, response):
            result = []
            for text in response.text_annotations:
                result.append(str(text.description))
            decorated_result, error_percentage, string_override = self.analyze_response_data(result[1:])
            return decorated_result, error_percentage, string_override