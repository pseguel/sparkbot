FROM ubuntu:14.04
MAINTAINER Paulo Seguel <pseguel@gmail.com>
FROM python:2.7
RUN pip install web.py
RUN pip install ciscosparkapi
RUN git clone https://github.com/pseguel/sparkbot.git
#CMD [ "python", "./bot.py"]

