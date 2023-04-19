FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Necessary Folders
COPY ../app ./app
COPY ../migrations ./migrations

# Necessary Files
COPY ../.env ../config.py ../run.py ../gunicorn.cfg ./

# Expose port
EXPOSE 8000

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
