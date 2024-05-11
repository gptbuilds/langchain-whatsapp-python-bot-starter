FROM python:3.12-slim-bullseye

# Upgrade pip
RUN pip install --upgrade pip

# Configure Poetry
ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Define work directories and user
ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/web
ENV LOG_DIR=/home/app/logs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Set work directory
WORKDIR $WORKDIR

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install

# Add user and group
RUN adduser --system --group $USER

# Create necessary directories and set permissions
RUN mkdir -p $APP_HOME $LOG_DIR $POETRY_CACHE_DIR \
    && chown -R $USER:$USER $APP_HOME $LOG_DIR $POETRY_CACHE_DIR \
    && chmod g+s $POETRY_CACHE_DIR

# Set work directory and copy application files
WORKDIR $APP_HOME
COPY . $APP_HOME
RUN chown -R $USER:$USER $APP_HOME

# Switch to non-root user
USER $USER
