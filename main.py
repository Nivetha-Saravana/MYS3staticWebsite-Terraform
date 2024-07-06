import os
import mimetypes
import boto3

def main():
    # Specify the directory containing your files (relative to the GitHub Actions workspace)
    directory = '.'  # Root directory of the repository
    bucket_name = 'Portfolioterraform'
    
    # Retrieve AWS credentials from environment variables
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    if aws_access_key_id is None or aws_secret_access_key is None:
        print("AWS credentials not found in environment variables.")
        return
    
    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    try:
        # List files in the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                local_file = os.path.join(root, file)
                s3_key = os.path.relpath(local_file, directory)  # Use relative path as the S3 key
                
                # Guess the content type based on the file extension
                content_type, _ = mimetypes.guess_type(local_file)
                if content_type is None:
                    content_type = 'binary/octet-stream'  # Default to binary if unknown
                
                # Upload the file with the correct content type
                s3.upload_file(
                    local_file, bucket_name, s3_key,
                    ExtraArgs={'ContentType': content_type}
                )
                print(f"Upload Successful: {local_file} to {s3_key} with Content-Type {content_type}")

    except FileNotFoundError:
        print(f"The directory {directory} was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()