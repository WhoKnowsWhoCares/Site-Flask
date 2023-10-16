FROM python:3.10-slim as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN mkdir -p /app
WORKDIR /app
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev,test --no-root


FROM python:3.10-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1
ENV FLASK_APP=wsgi.py \
    FLASK_DEBUG=False \
    FLASK_ENV=production \
    LOG_LEVEL='WARNING'

RUN apt-get update && apt-get install -y curl
WORKDIR /app
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
    
COPY --from=builder /app/.venv /app/.venv

# Necessary Files
COPY /app /app/app
COPY /migrations /app/migrations
COPY config.py wsgi.py /app/

# Expose port
EXPOSE 8000

# gunicorn
CMD ["gunicorn","-k","gevent","-w","1","-b","0.0.0.0:8000", "wsgi:app"]
# CMD ["python", "-m", "wsgi"]