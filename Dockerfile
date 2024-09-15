FROM python:3.12
# Create local working directory
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Copy all files from First_REST_API to current working directory
COPY . .
# Run commands
CMD ["/bin/bash", "docker-entrypoint.sh"]