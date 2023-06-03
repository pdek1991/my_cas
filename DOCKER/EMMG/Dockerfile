FROM python
#comment
WORKDIR /root/EMMG

COPY requirements.txt .
RUN pip install --no-cache-dir -r /root/EMMG/requirements.txt

VOLUME ["/root/EMMG"]

COPY . .
CMD ["python", "emmg.py"]
