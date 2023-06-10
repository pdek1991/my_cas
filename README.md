# my_cas

CAS:

CAS application using python which will have omi interface which is rest api based and accept /osm and /addpackage endpoints this data is to be stored in mysql db them emm component will generate string using this data and save to other table then cycler component will take this saved emm and carrousal it for period and repetion cycle as per defined values 

Version 1:
1. Accept requests over REST API interface 
2. OSM and ADD-Package command
3. Save data in mysql db
4. Generate EMM string using this data
5. Cycle it using stage and cycle configuration

DB Schema:
1. DB Schema:cas_pdek user:pdek pwd:pdek 
2. OSM Table which has Device ID 10 digit, message_text 160 char, message_id 8 char, Cycle period 2 char
3. Entitlement Table which will have Device-ID 10 digit, Package-IDs 30 char, Cycle period 2 char, Expiry date.
3. 


Version 2:
1. Support authentication and tokens for sending api requests
2. Add validation for checking duplicate package and msg id is OSM
3. Housekeeping of expired data
4. 


DB schema: cas
##create schema cas;
table name: generate_osm
##create table generate_osm (message_id INT, message_text VARCHAR(255), device_id INT);
USER:
CREATE USER 'omi_user'@'%' IDENTIFIED BY 'omi_user';
GRANT ALL PRIVILEGES ON *.* TO 'omi_user'@'%' WITH GRANT OPTION;

Addentitlement table
CREATE TABLE entitlements (device_id CHAR(10),package_id VARCHAR(40),expiry DATE);

Devices table:




docker build -t my_cas .
docker run -d --name my_cas -v /root/cas:/root/cas -p 5050:5050 -p 8081:8081 my_cas



### Important commands
sudo systemctl status NetworkManager


Elastic search enrollment token from virtualbox
eyJ2ZXIiOiI4LjYuMiIsImFkciI6WyIxNzIuMTcuMC4zOjkyMDAiXSwiZmdyIjoiNzU4N2Y5ODM3MjM5YzgzNzFmMjQ3ZTk1ZjMwZjRhYTYwYTRiNTliYWNjMGFmMDBmNDcyMjJjODY0MGI2N2Q1ZSIsImtleSI6ImtNY3RBNGNCVkZmQWlyc0VCUVlxOklqdVBWSDZEUl9XdG1XdlJWSlRZVXcifQ==



Elastic search enrollment token from docker desktop
eyJ2ZXIiOiI4LjYuMiIsImFkciI6WyIxNzIuMTcuMC4zOjkyMDAiXSwiZmdyIjoiNjk0NGJkNTg4MjgyMTJhYjBmMzYyZGY4ZjU3NDkwNDlkNzM0MmRjZmUxYWViZTc4ZmZiOWQwMzAzOWIyNDRjNSIsImtleSI6IjRqbnBCSWNCLXJlai0xb0p1STBOOlg3bG50b3BsVHlPV20xSVpaR29VX1EifQ==

SHA1 Fingerprint=97:A4:4D:37:1D:03:92:C9:B7:36:E4:A9:ED:3D:06:3F:8E:08:6D:C9


docker run --name kibana -d --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.7.0
docker run -d --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.7.0
docker run -d --name node-exporter --net elastic -p 9100:9100 prom/node-exporter
docker run -d --name prometheus --net elastic -p 9090:9090 prom/prometheus

docker run -d --name node-exporter --net elastic  -p 9100:9100 -v /root/metrics/:/home/ prom/node-exporter --collector.textfile.directory=/home/
  
  
docker run -d --name node-exporter --net elastic -p 9100:9100 -v "/root/metrics/:/host:ro,rslave" prom/node-exporter \
  --collector.textfile.directory=/host/

#Running with no volume when volume is attached user permission is getting changed
docker run -d --name node-exporter --net elastic  -p 9900:9100 prom/node-exporter --collector.textfile.directory=/home/


docker run -name mysqld-exporter -d -p 9104:9104 --net elastic prom/mysqld-exporter --config.my-cnf=

docker run -d  --name=mysql-exporter -p 9104:9104 -e DATA_SOURCE_NAME="omi_user:omi_user@(192.168.56.112:3306)"  prom/mysqld-exporter

#Install Node -exporter directly on host 

./node_exporter --collector.textfile.directory  /var/lib/node_exporter/textfile_collector


Oracle Exporter

docker run -it --rm -p 9161:9161 ghcr.io/iamseth/oracledb_exporter:0.5.0

docker run -d --name oracledb_exporter --link=oracle -p 9161:9161 -e DATA_SOURCE_NAME=oracle://pdek:pdek@192.168.56.200:1521/freepdb1 iamseth/oracledb_exporter:alpine



./elasticsearch-reset-password -u elastic -
./elasticsearch-reset-password -u elastic -i
./kibana-verification-code


docker run -d --name=metricbeat --user=root --volume="/var/run/docker.sock:/var/run/docker.sock:ro" docker.elastic.co/beats/metricbeat:latest metricbeat -e -E output.elasticsearch.hosts=["192.168.43.6:9200"]


GET kibana_sample_data_flights/_search
{
  "query": {
    "bool": {
      "must": [
        {"match": {"OriginCountry": "IN"}},
        {"match": {"DestCountry": "IT"}}
      ]
    }
  }
}





ftp://Reliance_JIO

Qru3HrfN@ftp.verimatrix.com




Install Kafka:

Download and extract
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties &
Test topic:
3. bin/kafka-topics.sh --create --topic topic_mycas --bootstrap-server 192.168.56.112:9092
Validate Topic details:
4. bin/kafka-topics.sh --describe --topic topic_mycas --bootstrap-server 192.168.56.112:9092
Add test line:
5. bin/kafka-console-producer.sh --topic topic_mycas --bootstrap-server 192.168.56.112:9092
Read message:
bin/kafka-console-consumer.sh --topic topic_mycas --from-beginning --bootstrap-server 192.168.56.112:9092
bin/kafka-console-consumer.sh --topic topic_mycas -bin/kafka-server-start.sh config/server.properties &
-bootstrap-server 192.168.56.112:9092


Docker Container
Dockerfile

docker ps --format "table {{.Names}}\t{{.Status}}"
docker build -t webapp .

docker run -d -p 8080:8080 -v /root/mycas/WEB-APP:/root/mycas/WEB-APP --name webapp webapp
docker run -d -p 5000:5000 -v /root/mycas/SMS-CAS:/root/mycas/SMS-CAS --name  sms-cas sms-cas
docker run -d  -v /root/EMMG:/root/EMMG --name  emmg emmg
docker run -d  -v /root/CYCLER:/root/CYCLER --name  cycler cycler
docker run -d  -v /root/CLIENT:/root/CLIENT --name  stb_client stb_client
docker run -d  -v /root/SCHEDULAR:/root/SCHEDULAR --name  schedular schedular

docker run -d  -v /root/STB:/root/STB --name stb stb


docker service create --name sms-cas --replicas 1 -p 5000:5000 --mount type=bind,source=/root/mycas/SMS-CAS,target=/root/mycas/SMS-CAS sms-cas

docker service create --name webapp --replicas 2 -p 8080:8080 --mount type=bind,source=/root/mycas/WEB-APP,target=/root/mycas/WEB-APP webapp

docker service create --name emmg --replicas 1 --mount type=bind,source=/root/mycas/EMMG,target=/root/mycas/EMMG wmmg

docker service create --name cycler --replicas 1 --mount type=bind,source=/root/mycas/CYCLER,target=/root/mycas/CYCLER cycler

docker service create --name client --replicas 1 --mount type=bind,source=/root/mycas/CLIENT,target=/root/mycas/CLIENT client

docker service create --name schedular --replicas 1 --mount type=bind,source=/root/mycas/SCHEDULAR,target=/root/mycas/SCHEDULAR schedular


docker service create --name stb --replicas 1 -p 9091:9091 --mount type=bind,source=/root/mycas/STB,target=/root/mycas/STB stb


docker run -it -e NGROK_AUTHTOKEN=2QPIR5lJbN8pZlBrPI4fp8cjPQG_2sgPGtWzvjCsUTPCS82xF ngrok/ngrok http 8080

docker run -it -e NGROK_AUTHTOKEN=2QPIR5lJbN8pZlBrPI4fp8cjPQG_2sgPGtWzvjCsUTPCS82xF ngrok/ngrok http --region=sa 192.168.56.102:8080

docker stack deploy -c docker-composr.yml mycas

docker service scale sms-cas=3

docker service update --replicas 5 sms-cas

