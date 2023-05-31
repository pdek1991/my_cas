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

