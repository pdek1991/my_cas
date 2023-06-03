FROM python
#comment
WORKDIR /root/SCHEDULAR

COPY requirements.txt .
RUN pip install --no-cache-dir -r /root/SCHEDULAR/requirements.txt

VOLUME ["/root/SCHEDULAR"]

COPY . .
CMD ["python", "schedular.py"]
