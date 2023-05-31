FROM python
#comment
WORKDIR /root/cas

COPY requirements.txt .
RUN pip install --no-cache-dir -r /root/cas/requirements.txt

VOLUME ["/root/cas"]

COPY . .

EXPOSE 5050
EXPOSE 8081
CMD ["python", "omi.py"]
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/bin/bash", "-c", "/entrypoint.sh &"]
