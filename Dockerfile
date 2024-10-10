# Base Image, means that container will have python 3.9 pre-installed
FROM python:3.9

# All instructions after this will be in /app
WORKDIR /app

# Copies all packages in requirements.txt and installs them.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copies all other files from current directory of the build into /app
# Make sure that the Dockerfile location is in the root, otherwise it might not download everything.
COPY . .

# Will execute main.py upon container being started.
CMD ["python", "main.py"]