!/bin/bash
# Install Docker
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Create a directory for Docker Compose files
mkdir ~/docker-compose

# Save Docker Compose configuration
echo '{docker_compose_config}' > ~/docker-compose/docker-compose.yml

# Change to the directory with Docker Compose files
cd ~/docker-compose

# Run Docker Compose
sudo docker-compose up -d