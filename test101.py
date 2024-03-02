import json
import boto3

images = {}
with open('test.jpg', 'rb') as file: images['test.jpg'] = file.read()


# with open(dog_jpg, 'rb') as file: images[dog_jpg] = file.read()

def query_endpoint(img):
    endpoint_name = 'jumpstart-dft-endpoint102'
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-image', Body=img,
                                      Accept='application/json;verbose')
    return response


def parse_prediction(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    predicted_label = model_predictions['predicted_label']
    labels = model_predictions['labels']
    probabilities = model_predictions['probabilities']
    return predicted_label, probabilities, labels


for filename, img in images.items():
    query_response = query_endpoint(img)
    predicted_label, probabilities, labels = parse_prediction(query_response)
    # display(HTML(f'<img src={filename} alt={filename} align="left" style="width: 250px;"/>'
    #              f'<figcaption>Predicted Label is : {predicted_label}</figcaption>'))
    print("PL" + predicted_label)

