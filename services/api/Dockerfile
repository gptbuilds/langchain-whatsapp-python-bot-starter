FROM python:3.12-slim-bullseye

# Install Poetry and clean up after installation
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Poetry and other configurations
ENV POETRY_HOME="/root/.local/share/pypoetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV WORKDIR="/usr/src/app"
ENV USER="app"
ENV APP_HOME="/home/app/web"
ENV LOG_DIR="/home/app/logs"
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR $WORKDIR

# Copy pyproject.toml and poetry.lock to the working directory
COPY ./pyproject.toml ./poetry.lock* $WORKDIR/

# Install dependencies using Poetry
RUN /root/.local/bin/poetry install --no-root

# Add a new system user and create necessary directories
RUN adduser --system --group $USER && \
    mkdir -p $APP_HOME && \
    mkdir -p $LOG_DIR

# Change the working directory to the application home
WORKDIR $APP_HOME

# Copy the application code to the container
COPY . $APP_HOME

# Set ownership of the application directory
RUN chown -R $USER:$USER $APP_HOME && \
    chown -R $USER:$USER $LOG_DIR

# Switch to the newly created user
USER $USER
