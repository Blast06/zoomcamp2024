 FROM python:3.9.1

 RUN pip install pandas
 RUN pip install  sqlalchemy
 RUN pip list
 WORKDIR  /app
 COPY ingest_data.py ingest_data.py
 COPY green_tripdata_2019-09.csv green_tripdata_2019-09.csv


 ENTRYPOINT ["python", "ingest_data.py"]

#  pip install <package_name>==<desired version>