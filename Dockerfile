FROM docker.io/library/golang:alpine3.20
COPY httpenv.go /go
RUN go build httpenv.go

FROM docker.io/library/alpine:3.20.1

RUN addgroup -g 1000 httpenv \
    && adduser -u 1000 -G httpenv -D httpenv
USER httpenv

COPY --from=0 --chown=httpenv:httpenv /go/httpenv /httpenv

EXPOSE 8888

CMD ["/httpenv"]
