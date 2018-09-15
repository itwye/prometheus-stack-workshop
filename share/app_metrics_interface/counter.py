from prometheus_client import Counter,start_http_server
import random
c = Counter('my_failures', 'Description of counter',["app","host"])
#c.inc()     # Increment by 1
#c.inc(1.6)  # Increment by given value


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests
    while True:
        c.labels("myselfapp","172.10.2.88").inc(random.randint(0,10))

