FROM python:3.11-slim as build

# APT update & upgrade
RUN apt-get update &&  \
    apt-get upgrade -y &&  \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Install poetry
ENV POETRY_VERSION=1.3.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

# prepare venv
COPY pyproject.toml poetry.lock ./
RUN python -m venv --copies ./venv
RUN . /venv/bin/activate && poetry install --only main

##### RUNNER
FROM python:3.11-slim AS runner

# APT update & upgrade
RUN apt-get update &&  \
    apt-get upgrade -y &&  \
    apt-get install -y uvicorn && \
    rm -rf /var/lib/apt/lists/*

# copy venv and add to path
COPY --from=build /venv /venv
ENV PATH /venv/bin:$PATH

# copy / run
COPY . ./

CMD [ "uvicorn", "src.main:app", "--host",  "0.0.0.0", "--port", "8000" ]
# docker build . -t demo:latest