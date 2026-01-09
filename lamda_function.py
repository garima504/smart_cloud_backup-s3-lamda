import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = 'garima-source-bucket'
    backup_bucket = 'garima-backup-bucket'

    for record in event['Records']:
        key = urllib.parse.unquote_plus(
            record['s3']['object']['key']
        )

        try:
            # Copy object from source bucket to backup bucket
            copy_source = {
                'Bucket': source_bucket,
                'Key': key
            }

            s3.copy_object(
                CopySource=copy_source,
                Bucket=backup_bucket,
                Key=key
            )

            print(f"Backup successful for: {key}")

        except Exception as e:
            print(f"Error during backup: {e}")
            raise e
