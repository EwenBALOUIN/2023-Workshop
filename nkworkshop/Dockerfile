FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /nkworkshop
COPY requirements.txt /nkworkshop/
RUN pip install -r requirements.txt
COPY . /nkworkshop/
