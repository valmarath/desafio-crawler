FROM python:3.10

ADD crawler_gabriel_valmarath.py .

RUN pip install requests beautifulsoup4 pandas pymongo json selenium pillow schedule time

CMD ["python", "./crawler_gabriel_valmarath.py"]