# builds python 3.8
FROM python:3.8-buster
WORKDIR /app
ADD . .
CMD ["python","./hello.py"]
# EXPOSE 8000
# CMD ["python","-m", "http.server"]