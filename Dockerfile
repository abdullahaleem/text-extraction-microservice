FROM python:3.8-slim

COPY ./entrypoint.sh /entrypoint.sh
COPY ./app /app
COPY ./requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install  -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc

RUN pip3 install -r requirements.txt

# pruning commanads that deletes things we dont need anymore to slim down our enivronment
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# want to make sure our entry point is executable
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]

