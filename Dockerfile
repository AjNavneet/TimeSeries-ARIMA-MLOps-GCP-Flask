FROM tiangolo/uwsgi-nginx:python3.7

ADD ./MLPipeline /app/MLPipeline
ADD ./input /app/input
ADD ./output /app/output
ADD requirements.txt /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt
ADD uwsgi.ini /app
ADD __init__.py /app
ADD main.py /app