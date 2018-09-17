FROM ubuntu:18.04 as build
LABEL maintainer daikeren@gmail.com

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PIP_WHEEL_DIR=/root/wheelhouse

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-dev python3-pip build-essential && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

COPY Pipfile* /app/
WORKDIR /app
RUN mkdir /root/wheelhouse && pip3 install wheel pipenv && \
    pipenv lock -r > /tmp/requirements.txt && \
    pip3 wheel -r /tmp/requirements.txt

FROM build
EXPOSE 8000

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PIP_FIND_LINKS=/root/wheelhouse
ENV DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.production

COPY --from=build /tmp/requirements.txt /tmp/requirements.txt
COPY --from=build /root/wheelhouse /root/wheelhouse

RUN apt-get update && \
    apt-get install -y --no-install-recommends make python3-pkg-resources python3-setuptools python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN pip3 install -r /tmp/requirements.txt

COPY . /app

CMD ["gunicorn", "-b", ":8000", "{{cookiecutter.project_slug}}.wsgi", "--access-logfile", "-", "--error-logfile", "-"]
