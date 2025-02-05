# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY fetch_commits.py .

# Install dependencies
RUN pip install requests

# Run the script
CMD ["python", "fetch_commits.py"]
