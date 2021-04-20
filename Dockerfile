FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/poketch
WORKDIR /opt/poketch
ADD requirements.txt /opt/poketch
RUN pip install — upgrade pip && pip install -r requirements.txt
ADD . /opt/poketch