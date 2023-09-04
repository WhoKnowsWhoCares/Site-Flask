FROM python:3.10-slim as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
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
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root


FROM python:3.10-slim as base

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
ENV FLASK_APP=wsgi.py \
    FLASK_DEBUG=0 \
    FLASK_ENV=production

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
    
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
WORKDIR /app

# Necessary Files
COPY /app/ ./app/
COPY /migrations/ ./migrations/
COPY .env config.py wsgi.py ./

# Expose port
EXPOSE 8000

# gunicorn
CMD ["gunicorn","-k","gevent","-w","1","-b","0.0.0.0:8000", "wsgi:app"]