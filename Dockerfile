# Use an official Python runtime as a parent image
FROM python:3.9.11

# Set the working directory in the container to /zmbner
WORKDIR /zmbner

# Copy the requirements file into the container at /zmbner
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /zmbner
COPY . /zmbner

# Run bash when the container launches
CMD ["/bin/bash"]