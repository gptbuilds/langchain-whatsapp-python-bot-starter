FROM python:3.12-slim-bullseye

# Install Poetry and clean up after installation
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Poetry
ENV POETRY_HOME=/root/.local/share/pypoetry
ENV PATH="$POETRY_HOME/bin:$PATH"

# Verify Poetry installation
RUN poetry --version

# Set work directories and environment variables
ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/web
ENV LOG_DIR=/home/app/logs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR $WORKDIR

# Copy pyproject.toml and poetry.lock
COPY ./pyproject.toml ./poetry.lock* $WORKDIR/

# Install dependencies
RUN poetry install --no-root

# Add user and set permissions
RUN adduser --system --group $USER
RUN mkdir -p $APP_HOME
RUN mkdir -p $LOG_DIR
WORKDIR $APP_HOME

COPY . $APP_HOME
RUN chown -R $USER:$USER $APP_HOME
RUN chown -R $USER:$USER $LOG_DIR
USER $USER
