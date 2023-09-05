from constructs import Construct
from cdktf import TerraformStack, TerraformOutput
from imports.aws import Instance, SecurityGroup

class EC2Stack(TerraformStack):
    def __init__(self, scope: Construct, id: str, vpc_id: str, sg_id: str):
        super().__init__(scope, id)

        # Create a security group
        security_group = SecurityGroup(self, "MyEC2SecurityGroup",
            name="my-ec2-security-group",
            vpc_id=vpc_id,
            # Define inbound and outbound rules as needed
        )

        # Create an EC2 instance
        ec2_instance = Instance(self, "MyEC2Instance",
            ami="ami-12345678",  # Specify the AMI ID
            instance_type="t2.micro",  # Specify the instance type
            vpc_security_group_ids=[security_group.id],
            # Define other instance properties, such as user data to install software
        )

        # Output the EC2 instance ID
        TerraformOutput(self, "EC2InstanceId", value=ec2_instance.id)
