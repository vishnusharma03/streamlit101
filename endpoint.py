import json
import boto3
from botocore.config import Config

my_config = Config(
    read_timeout=120,  # Time in seconds
    connect_timeout=120  # Time in seconds
)


# endpoint_name = 'jumpstart-dft-pt-ic-resnet50'
# img = open('test.jpg', 'rb').read()
class Query:
    def __init__(self, endpoint_name):
        self.endpoint_name = endpoint_name

    def query_endpoint(self, img):
        client = boto3.client('runtime.sagemaker', config=my_config)
        response = client.invoke_endpoint(
            EndpointName=self.endpoint_name,
            ContentType='application/x-image',
            Body=img,
            Accept='application/json;verbose'
        )
        return response

    @staticmethod
    def parse_prediction(query_response):
        model_predictions = json.loads(query_response['Body'].read())
        predicted_label = model_predictions['predicted_label']
        #labels = model_predictions['labels']
        #probabilities = model_predictions['probabilities']
        return predicted_label
    # def parse_prediction(query_response):
    #     predictions = json.loads(query_response['Body'].read())
    #     return predictions

# import json
# import boto3
#
# class query:
#     def __init__(self, img):
#         self.img = img
#
#     def query_endpoint(self):
#         endpoint_name = 'jumpstart-dft-pt-ic-resnet50'
#         client = boto3.client('runtime.sagemaker')
#         response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-image', Body=self.img, Accept='application/json;verbose')
#         return response
#
#     def parse_prediction(query_response):
#         model_predictions = json.loads(query_response['Body'].read())
#         predicted_label = model_predictions['predicted_label']
#         labels = model_predictions['labels']
#         probabilities = model_predictions['probabilities']
#         return predicted_label, probabilities, labels
#
#     def display:
#         for filename, img in images.items():
#             query_response = query_endpoint(img)
#             predicted_label, probabilities, labels = parse_prediction(query_response)
#             display(HTML(f'<img src={filename} alt={filename} align="left" style="width: 250px;"/>'
#             f'<figcaption>Predicted Label is : {predicted_label}</figcaption>'))
