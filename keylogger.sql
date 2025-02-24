create database keylogger;
use keylogger;

-- table to store screenshots 
CREATE TABLE SCREENSHOT(SSID INTEGER AUTO_INCREMENT, Filename VARCHAR(255) NOT NULL,
IMAGE LONGBLOB NOT NULL, UPLOAD_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(SSID, Filename));

-- table to store audio files 
CREATE TABLE AUDIO(ADID INTEGER AUTO_INCREMENT, Filename VARCHAR(255) NOT NULL,
AUDIO_DATA LONGBLOB NOT NULL, UPLOAD_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(ADID, Filename));

-- table to store system information 
CREATE TABLE SYSTEM_INFO(Parameter VARCHAR(255), Value TEXT);

select * from screenshot;
select * from audio;
select * from system_info;

truncate table screenshot;
truncate table audio;
truncate table system_info;