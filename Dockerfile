FROM python:3.9-slim
WORKDIR /app2
COPY app_stema.py /app2
COPY templates/ /app2/templates
COPY static/ /app2/static
RUN pip install flask
EXPOSE 5000
CMD ["python3","app_stema.py"]
