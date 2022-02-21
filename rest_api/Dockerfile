FROM python
RUN mkdir -p /app2/
WORKDIR /app2/
COPY . /app2/
RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
VOLUME ["/app2/data"]
ENV PORT 8000
EXPOSE $PORT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]





