# Inherit from the Python Docker image
FROM python:3.7-slim

# Copy the source code to app folder
# https://nickjanetakis.com/blog/docker-tip-2-the-difference-between-copy-and-add-in-a-dockerile
ADD ./ /app/

# Install requirements
RUN pip install -r /app/requirements.txt

# Change the working directory
WORKDIR /app/

# Set the command as the script name
CMD ["python","-u","api.py"]