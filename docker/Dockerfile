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

FROM gcr.io/distroless/python3-debian12@sha256:e8e50bc861b16d916f598d7ec920a8cef1e35e99b668a738fe80c032801ceb78


RUN addgroup -g 1000 httpenv \
    && adduser -u 1000 -G httpenv -D httpenv
USER httpenv

COPY --from=build-venv /venv /venv

COPY app/main.py .

ENTRYPOINT ["/venv/bin/python3", "main.py"]
