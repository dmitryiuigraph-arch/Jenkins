FROM python:3.9-slim
CMD python -m http.server 5000 --bind 0.0.0.0
