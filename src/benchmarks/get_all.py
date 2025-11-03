from repositories.mongo_repository import MongoRepository
from repositories.postgres_repository import PostgresRepository
from datetime import datetime
import logging


repeat_times = 200

logging.basicConfig(level=logging.INFO)

logging.info("STARTING MONGO BENCHMARK")
mongo_elapsed_time = 0
for i in range(0, repeat_times):
    start_time = datetime.now()
    MongoRepository.find_with_parameters()
    mongo_elapsed_time += (datetime.now() - start_time).total_seconds()
logging.info(f"FINISHED MONGO BENCHMARK: {mongo_elapsed_time} seconds elapsed")


logging.info("STARTING POSTGRES BENCHMARK")
pg_elapsed_time = 0
for i in range(0, repeat_times):
    start_time = datetime.now()
    PostgresRepository.find_with_parameters()
    pg_elapsed_time += (datetime.now() - start_time).total_seconds()
logging.info(f"FINISHED POSTGRES BENCHMARK: {pg_elapsed_time} seconds elapsed")