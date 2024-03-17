# python image
FROM python:3.12

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set up directory to work in contener
WORKDIR /code

COPY requirements.txt /code/

# install dependence from file requirements.txt
RUN pip install -r requirements.txt

# copy all kod from app to working directory
COPY . /code/