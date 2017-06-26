# WaterSoftenerMonitor

This is some stuff I use to monitor my water softner.  

General setup:

Use a RaspberryPI (any model ought to do it, as long as you have networking functional) and assemble a distance device as indicated by the link below[1]. Attach the ultrasonic sensor to the underside of the lid of the water softener, and the RasberryPI on the outside.  Set up the `distance.py` script to run as a cron job every minute.  Set up a webserver (I used `lighttpd`, but anything that can serve a static JSON will due) to serve the file. 

Next, set up some metrics gathering service to obtain the numbers.  Ive used Datadog, Telegraf/InfluxDB/Grafana, and Promethous in various itterations. 

[1] https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi 
