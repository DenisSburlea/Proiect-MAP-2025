FROM python:3.10-slim

WORKDIR /app

COPY src/main.py ./

RUN chmod +x main.py

ENTRYPOINT [ "./main.py" ]

CMD ["--help"]