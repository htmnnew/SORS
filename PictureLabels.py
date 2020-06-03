import io
from google.cloud import vision
import os

#JSON file to grant access for google vision api
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="V:\\Nerses\\My First Project-6a20a20acb02.json"

#Image Labeler based on the content of the image
def detect_labels(path):
    """Detects web annotations given an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    hold = []

    #Loop provide label descriptions of the image
    #for later search to categorize the picture file
    for label in labels:
        hold.append(label.description)
    return hold
