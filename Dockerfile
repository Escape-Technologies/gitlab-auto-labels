FROM python:3.10-alpine3.15

WORKDIR /app/
RUN apk add git
RUN git config --global --add safe.directory /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY auto_labels auto_labels
COPY setup.py .

RUN python setup.py install

WORKDIR /src/

ENTRYPOINT [ "/bin/sh" ]
CMD ["-c", "python3.10 -m auto_labels"]
