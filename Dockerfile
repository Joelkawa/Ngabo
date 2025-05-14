FROM python:3.12.4-slim-bullseye

#Set Environment variables
ENV PIP_DISABLE_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Working Directory
WORKDIR /Ngabo

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y libpq-dev gcc

#copy and install the requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY .  .
# Run the application
CMD gunicorn family_project.wsgi:application --bind 0.0.0.0:8000
