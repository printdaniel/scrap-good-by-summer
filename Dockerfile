FROM postgres

RUN mkdir -p /home/app
COPY . /home/app 

EXPOSE 5432 

CMD ["python view.py", "/home/app/view.py"]
