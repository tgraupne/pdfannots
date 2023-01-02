FROM python:3.10-slim

RUN groupadd -g 1000 python \
  && useradd --create-home --no-log-init -u 1000 -g 1000 python

USER python

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir --no-warn-script-location pdfannots

ENTRYPOINT ["/home/python/.local/bin/pdfannots"]
