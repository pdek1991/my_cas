FROM python
#comment
WORKDIR /root/WEB-APP

COPY requirements.txt .

RUN pip install --no-cache-dir -r /root/WEB-APP/requirements.txt

VOLUME ["/root/WEB-APP"]

COPY . .

EXPOSE 5005
EXPOSE 8080
CMD ["python", "webpage.py"]
