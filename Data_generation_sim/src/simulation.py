import simpy
import random
import numpy as np

def traffic_simulation(arrival_rate, service_rate, counters, sim_time):

    env = simpy.Environment()
    server = simpy.Resource(env, capacity=counters)

    waiting_times = []
    queue_lengths = []

    def car(env):
        arrival = env.now
        with server.request() as request:
            yield request
            wait = env.now - arrival
            waiting_times.append(wait)

            service_time = random.expovariate(service_rate)
            yield env.timeout(service_time)

    def arrival_process(env):
        while True:
            yield env.timeout(random.expovariate(arrival_rate))
            env.process(car(env))
            queue_lengths.append(len(server.queue))

    env.process(arrival_process(env))
    env.run(until=sim_time)

    avg_wait = np.mean(waiting_times) if waiting_times else 0
    max_queue = max(queue_lengths) if queue_lengths else 0

    return avg_wait, max_queue
