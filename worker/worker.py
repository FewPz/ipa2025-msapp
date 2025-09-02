from consumer import consume
import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
consume(RABBITMQ_HOST)
