FROM docker.io/debian:bookworm-slim AS build

LABEL org.opencontainers.image.source=https://github.com/irish1986/http-micro-server
LABEL org.opencontainers.image.description="a simple http-micro-server"
LABEL org.opencontainers.image.licenses=MIT

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

FROM build AS build-venv

COPY requirements.txt /requirements.txt

RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM gcr.io/distroless/python3-debian12@sha256:5c732dbcb05a53ffa7d3e9094bfa75b27eeaf5df6edf116d552414e010d124a2


RUN addgroup -g 1000 httpenv \
    && adduser -u 1000 -G httpenv -D httpenv
USER httpenv

COPY --from=build-venv /venv /venv

COPY app/main.py .

ENTRYPOINT ["/venv/bin/python3", "main.py"]
