FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade fastapi uvicorn


FROM alpine

COPY quickstart.sh /
CMD ["/quickstart.sh"]