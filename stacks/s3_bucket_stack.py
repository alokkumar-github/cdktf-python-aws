from constructs import Construct
from cdktf import TerraformStack, TerraformOutput
from imports.aws import S3Bucket

class S3BucketStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Create an S3 bucket
        s3_bucket = S3Bucket(self, "MyS3Bucket",
            bucket="my-unique-s3-bucket-name",  # Replace with your desired bucket name
            acl="private",  # Set the bucket ACL (Access Control List)
        )

        # Output the S3 bucket name
        TerraformOutput(self, "S3BucketName", value=s3_bucket.id)
