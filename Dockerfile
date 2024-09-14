FROM python:3.12
LABEL authors="bochj"

EXPOSE 5000
# Create local working directory
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy all files from First_REST_API to current working directory
COPY . .
# Run commands
CMD ["flask", "run", "--host", "0.0.0.0"]