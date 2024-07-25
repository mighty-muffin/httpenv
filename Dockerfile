FROM docker.io/library/golang:1.20.14-alpine3.19 AS build
COPY httpenv.go /go
RUN go build httpenv.go

FROM docker.io/library/alpine:3.19

RUN addgroup -g 1000 httpenv \
    && adduser -u 1000 -G httpenv -D httpenv
USER httpenv

COPY --from=build --chown=httpenv:httpenv /go/httpenv /httpenv

EXPOSE 8888

CMD ["/httpenv"]
