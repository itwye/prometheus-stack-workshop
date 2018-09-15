from prometheus_client import Gauge, start_http_server
import random
g = Gauge('my_inprogress_requests', 'Description of gauge')
#g.inc()      # Increment by 1
#g.dec(10)    # Decrement by given value
#g.set(4.2)   # Set to a given value

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests
    while True:
        g.set(1024*1024*100)   # Set to a given value
        g.dec(1024*1024*random.randint(0,100))    # Decrement by given value
        g.inc(1024*1024*random.randint(0,100))   # Set to a given value

