 FROM python:3.9.1

 RUN pip install pandas
 RUN pip install psycopg2
 RUN pip install  sqlalchemy
 WORKDIR  /app
 COPY pipeline.py pipeline.py
 COPY yellow_tripdata_2021-01.csv yellow_tripdata_2021-01.csv


 ENTRYPOINT ["python", "pipeline.py"]

#  pip install <package_name>==<desired version>