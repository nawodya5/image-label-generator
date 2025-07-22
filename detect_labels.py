import boto3

def detect_labels_s3(bucket, photo):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10,
        MinConfidence=70
    )

    print("Detected labels in " + photo)
    for label in response['Labels']:
        print(f"{label['Name']} : {round(label['Confidence'], 2)}%")

# Replace with your S3 bucket name and image file name
bucket_name = 'recognitionbucket1'
image_name = 'gray-elephant.jpg'

detect_labels_s3(bucket_name, image_name)
