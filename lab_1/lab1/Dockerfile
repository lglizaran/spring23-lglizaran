FROM python:3.11-slim as build

# APT update & upgrade
RUN set -eux; \
    apt-get update; \
    apt-get upgrade -y; \
    rm -rf /var/lib/apt/lists/*


# RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends sudo htop cron curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH /root/.local/bin:$PATH

# copy TOML and poetru
COPY pyproject.toml poetry.loc ./

# install dependencies
RUN python -m venv --copies ./venv
RUN . ./venv/bin/activate && poetry install --only main

##### RUNNER
FROM python:3.11-slim AS runner

# APT update & upgrade
RUN set -eux; \
    apt-get update; \
    apt-get upgrade -y; \
    rm -rf /var/lib/apt/lists/*

# update Paths  
COPY --from=build /venv /venv
ENV PATH /venv/bin:$PATH

# copy / run
COPY . ./

CMD ['uvicorn', 'src.main:app', '--port', '8000', '--host'. '0.0.0.0']
# docker build . -t demo:latest