import random
import pandas as pd
from src.simulation import traffic_simulation

def generate_dataset(n_simulations=1000):

    data = []

    for _ in range(n_simulations):

        arrival_rate = random.uniform(1, 10)
        service_rate = random.uniform(2, 15)
        counters = random.randint(1, 5)
        sim_time = random.randint(100, 500)

        avg_wait, max_queue = traffic_simulation(
            arrival_rate, service_rate, counters, sim_time
        )

        data.append([
            arrival_rate,
            service_rate,
            counters,
            sim_time,
            avg_wait,
            max_queue
        ])

    columns = [
        "arrival_rate",
        "service_rate",
        "counters",
        "sim_time",
        "avg_wait",
        "max_queue"
    ]

    df = pd.DataFrame(data, columns=columns)
    return df
