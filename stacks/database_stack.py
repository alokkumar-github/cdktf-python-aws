# pip install cdktf-postgresql

from constructs import Construct
from cdktf import TerraformStack, TerraformOutput
from imports.cdktf import PostgresqlProvider, PostgresqlDatabase

class DatabaseStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Define the PostgreSQL provider
        postgres_provider = PostgresqlProvider(self, "MyPostgresProvider",
            host="<postgres-hostname>",  # Use the appropriate hostname
            port=5432,  # Default PostgreSQL port
            user="myuser",  # User defined in docker-compose.yml
            password="mypassword",  # Password defined in docker-compose.yml
            database="mydb",  # Database name defined in docker-compose.yml
        )

        # Create a PostgreSQL database
        postgres_db = PostgresqlDatabase(self, "MyDatabase",
            provider=postgres_provider,
            name="mydb",
        )

        # Output the database details
        TerraformOutput(self, "DatabaseEndpoint", value=postgres_db.endpoint)
