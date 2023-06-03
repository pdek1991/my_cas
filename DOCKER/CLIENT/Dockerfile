FROM python
#comment
WORKDIR /root/CLIENT

COPY requirements.txt .
RUN pip install --no-cache-dir -r /root/CLIENT/requirements.txt

VOLUME ["/root/CLIENT"]

COPY . .
CMD ["python", "stb_client.py"]
