#!/usr/bin/env python
# --------------------------------
# Running metrics interface of your application
# --------------------------------

import socket
import random
from prometheus_client import Gauge, Counter, start_http_server

appname = "order"
hostname = socket.gethostname()

# -------------------------
# http_requests_total
# -------------------------

c = Counter('http_requests_total', 'total number of http requests for application by response status',["app","host","status"])

def httpRequestTotal():
    c.labels(appname,hostname,"200").inc(random.randint(5,10))
    c.labels(appname,hostname,"502").inc(random.randint(0,3))
    c.labels(appname,hostname,"404").inc(random.randint(0,3))

# ------------------------
# app_used_memory
# ------------------------

g = Gauge('app_used_memory', 'used memory for applications',["app","host"])

def appUsedMemory():
    g.labels(appname,hostname).set(1024*1024*100)   
    g.labels(appname,hostname).dec(1024*1024*random.randint(0,100))   
    g.labels(appname,hostname).inc(1024*1024*random.randint(0,100))  

# -----------------------
# main
# -----------------------

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8001)
    # Generate some requests
    while True:
        httpRequestTotal()
        appUsedMemory()



