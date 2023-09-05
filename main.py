#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import AwsProvider, Instance, SecurityGroup

from stacks.vpc_stack import VpcStack
from stacks.s3_bucket_stack import S3BucketStack

from stacks.security_group_stack import SecurityGroupStack
from stacks.ec2_stack import EC2Stack  # Import the EC2 stack



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here

        # Define the AWS provider
        aws_provider = AwsProvider(self, "MyAwsProvider", region="us-east-1")

        # # Create a security group
        # security_group = SecurityGroup(self, "MySecurityGroup",
        #     vpc_id="<your-vpc-id>",
        #     description="My security group",
        # )

        # # Define the EC2 instance
        # ec2_instance = Instance(self, "MyEC2Instance",
        #     ami="<your-ami-id>",
        #     instance_type="t2.micro",
        #     subnet_id="<your-subnet-id>",
        #     security_groups=[security_group.id],  # Attach the security group
        # )

        # Define the Docker Compose service
        # docker_compose = DockerComposeApp(self, "MyDockerCompose",
        #     project_name="myapp",
        #     cwd="./",  # Path to the directory containing docker-compose.yml
        # )

        # Read user data from the file
        with open("user_data.sh", "r") as user_data_file:
            user_data_script = user_data_file.read()

        docker_compose = DockerComposeApp(self, "MyDockerCompose",
            project_name="myapp",
            cwd="./",  # Path to the directory containing docker-compose.yml
            depends_on=["postgres"],  # Add this line
        )

        # Include the S3BucketStack
        S3BucketStack(self, "MyS3BucketStack")

        #Create a VPC Stack (replace this with your actual VPC stack)
        vpc_stack = YourVpcStack(self, "MyVPCStack")

        # Use the SecurityGroupStack and pass the VPC ID
        security_group_stack = SecurityGroupStack(self, "MySecurityGroupStack", vpc_id=vpc_stack.vpc_id)

        # Create the EC2 stack and pass VPC ID and Security Group ID
        ec2_stack = EC2Stack(self, "MyEC2Stack", vpc_id=vpc_stack.vpc_id, sg_id=security_group_stack.security_group_id , user_data=user_data_script )

        # Output the public IP of the EC2 instance
        TerraformOutput(self, "InstancePublicIp", value=ec2_instance.public_ip)


app = App()
MyStack(app, "cdktf-python-aws")

# VpcStack(app, "MyVpcStack")  # Include the VpcStack

app.synth()
