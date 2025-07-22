🖼️ Image Labels Generator using Amazon Rekognition

This project uses **Amazon Rekognition** to detect objects, scenes, and concepts in an image stored in an **Amazon S3 bucket**, and prints the labels with their confidence scores using Python.

📌 Features

- Detects image labels using AWS Rekognition
- Supports image input from Amazon S3
- Shows confidence percentages for each detected label
- Simple Python script using Boto3

🛠️ Tech Stack

- Python 3.x
- AWS Rekognition
- Amazon S3
- Boto3 (AWS SDK for Python)

📁 Folder Structure

```

image-label-generator/
├── detect\_labels\_s3.py       # Main script
├── requirements.txt          # Python dependencies
└── README.md                 # This file

````

## 🔧 Installation

### 1. Clone this repo

```bash
git clone https://github.com/your-username/image-label-generator.git
cd image-label-generator
````

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set up AWS credentials

Configure your AWS credentials to allow access to Rekognition and S3:



aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY


region = us-east-1


4. Upload Image to S3

Upload your image (e.g., `dog.jpg`) to an S3 bucket using the AWS console.

▶️ How to Run

Edit the `detect_labels_s3.py` file and replace the bucket name and image filename:

python
bucket_name = 'your-bucket-name'
image_name = 'your-image-name.jpg'


Then run:

bash
python detect_labels_s3.py


📌 Sample Output

```
Detected labels in dog.jpg
Dog : 98.6%
Pet : 94.2%
Animal : 93.1%
Canine : 91.7%
```

📜 License

This project is licensed under the MIT License.

🙋‍♂️ Author

Dulaj Nawodya
Undergraduate, University of Colombo
