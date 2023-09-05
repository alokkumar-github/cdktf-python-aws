from constructs import Construct
from cdktf import TerraformStack, TerraformOutput
from imports.aws import SecurityGroup, SecurityGroupRule

class SecurityGroupStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, vpc_id: str):
        super().__init__(scope, id)

        # Create a security group
        security_group = SecurityGroup(self, "MySecurityGroup",
            name="my-security-group",
            vpc_id=vpc_id,  # Specify the VPC ID
        )

        # Define inbound rules
        SecurityGroupRule(self, "InboundRuleSSH",
            type="ingress",
            from_port=22,
            to_port=22,
            protocol="tcp",
            cidr_blocks=["0.0.0.0/0"],  # Allow SSH access from anywhere (for demonstration purposes)
            security_group_id=security_group.id,
        )

        SecurityGroupRule(self, "InboundRuleHTTP",
            type="ingress",
            from_port=80,
            to_port=80,
            protocol="tcp",
            cidr_blocks=["0.0.0.0/0"],  # Allow HTTP access from anywhere (for demonstration purposes)
            security_group_id=security_group.id,
        )

        # Define outbound rule
        SecurityGroupRule(self, "OutboundRuleAllTraffic",
            type="egress",
            from_port=0,
            to_port=0,
            protocol="-1",
            cidr_blocks=["0.0.0.0/0"],  # Allow all outbound traffic (for demonstration purposes)
            security_group_id=security_group.id,
        )

        # Output the security group ID
        TerraformOutput(self, "SecurityGroupId", value=security_group.id)
