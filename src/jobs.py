from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path) as file:
        list = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in list:
            jobs_list.append(job)
    return jobs_list
