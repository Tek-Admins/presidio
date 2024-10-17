FROM python:3.9-slim

ARG NAME
ENV PIP_NO_CACHE_DIR=1
WORKDIR /usr/bin/${NAME}

COPY ./pyproject.toml /usr/bin/${NAME}/
COPY ./README.md /usr/bin/${NAME}/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install poetry && poetry install --no-root --only=main -E server

COPY . /usr/bin/${NAME}/

#EXPOSE ${PORT}
EXPOSE 5001:3000
CMD poetry run python app.py