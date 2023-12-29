FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Stuff for pyodbc to install correctly in image and run correctly in container
ENV ACCEPT_EULA=Y
RUN apt-get update -y \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools

COPY requirements.txt /

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /server
WORKDIR /server

# Copy project code.
COPY . /server/

EXPOSE 8000