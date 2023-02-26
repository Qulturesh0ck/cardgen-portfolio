# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /backend


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


COPY . .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

ENV FLASK_APP=wsgi.py

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["flask", "run", "--host", "0.0.0.0:5000"]
