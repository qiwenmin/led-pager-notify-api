FROM python:alpine
COPY ./src /app
RUN cd /app && \
    pip install -i https://pypi.mirrors.ustc.edu.cn/simple -r requirements.txt

EXPOSE 8000

WORKDIR /app
ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "app:app" ]
