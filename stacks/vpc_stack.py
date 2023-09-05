from constructs import Construct
from cdktf import TerraformStack
from imports.aws import Vpc, Subnet, InternetGateway, RouteTable, Route, RouteTableAssociation

class VpcStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Create a VPC
        vpc = Vpc(self, "MyVpc",
            cidr_block="10.0.0.0/16",
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )

        # Create a public subnet
        public_subnet = Subnet(self, "PublicSubnet",
            vpc_id=vpc.id,
            cidr_block="10.0.0.0/24",
            map_public_ip_on_launch=True,
        )

        # Create an internet gateway
        internet_gateway = InternetGateway(self, "MyInternetGateway",
            vpc_id=vpc.id,
        )

        # Create a route table and associate it with the public subnet
        route_table = RouteTable(self, "PublicRouteTable",
            vpc_id=vpc.id,
        )

        RouteTableAssociation(self, "PublicSubnetAssociation",
            subnet_id=public_subnet.id,
            route_table_id=route_table.id,
        )

        # Create a default route to the internet gateway
        Route(self, "DefaultRoute",
            route_table_id=route_table.id,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=internet_gateway.id,
        )
