FROM python
#comment
WORKDIR /root/CYCLER

COPY requirements.txt .
RUN pip install --no-cache-dir -r /root/CYCLER/requirements.txt

VOLUME ["/root/CYCLER"]

COPY . .
CMD ["python", "cycler.py"]
