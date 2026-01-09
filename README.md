# smart_cloud_backup-s3-lamda
This project implements an event-driven, serverless cloud backup solution using Aws Lamda And S3.
It automatically creates a backup of files uploaded to a s3 bucket ensure data safety even if the source files are deleted.
# Technologies
1.AWS Lamda
2.Amazon S3
3.Python(boto 3)
# Working of the Project
1. A file is uploaded to the source S3 bucket.
2. The upload event triggers an AWS Lambda function.
3. The Lambda function copies the file to a backup S3 bucket.
4. The backup file remains available even if the source file is deleted.
 # Key Features
1. Automatic file backup
2. Event-driven execution
3.Serverless architecture
4. Helps prevent data loss
## Learning Outcome
1. Understanding AWS Lambda and S3 integration
2. Working with event-based cloud services
3. Basic knowledge of IAM roles and permissions
