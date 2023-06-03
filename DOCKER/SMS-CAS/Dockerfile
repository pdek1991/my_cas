FROM python
#comment
WORKDIR /root/SMS-CAS

COPY requirements.txt .

RUN pip install --no-cache-dir -r /root/SMS-CAS/requirements.txt

VOLUME ["/root/SMS-CAS"]

COPY . .

EXPOSE 5000
EXPOSE 8080
CMD ["python", "omi.py"]
