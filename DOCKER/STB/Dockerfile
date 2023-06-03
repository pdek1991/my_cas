FROM python
#comment
WORKDIR /root/STB

COPY requirements.txt .
RUN pip install --no-cache-dir -r /root/STB/requirements.txt

VOLUME ["/root/STB"]

COPY . .
CMD ["python", "stb.py"]
