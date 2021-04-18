FROM python:3.9.0

COPY requirments.txt ./

RUN pip install -r requirments.txt

COPY task1.py .

EXPOSE 5000

CMD python task1.py