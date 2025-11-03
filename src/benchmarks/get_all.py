from repositories.mongo_repository import MongoRepository
from repositories.postgres_repository import PostgresRepository
from datetime import datetime
import logging


repeat_times = 500

logging.basicConfig(level=logging.INFO)


print("::: BUSCAR TODOS OS DOCUMENTOS :::")
print(f"::: REPETIR {repeat_times} VEZES")


print("\n======= MongoDB =======")
mongo_start_time = datetime.now()
total_documents = 0
for i in range(0, repeat_times):
    results = MongoRepository.find_with_parameters()
    total_documents += len(results)
mongo_finish_time = datetime.now()
print(f"::: {total_documents} DOCUMENTOS BUSCADOS")
print(f"::: EM {mongo_finish_time - mongo_start_time}")
print("=======================\n")

print("======= PostgreSQL =======")
pg_start_time = datetime.now()
total_documents = 0
for i in range(0, repeat_times):
    results = PostgresRepository.find_with_parameters()
    total_documents += len(results)
pg_finish_time = datetime.now()
print(f"::: {total_documents} DOCUMENTOS BUSCADOS")
print(f"::: EM {pg_finish_time - pg_start_time}")
print("==========================")