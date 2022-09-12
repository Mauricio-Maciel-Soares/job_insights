from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for index in content:
            jobs_list.append(index)
    return jobs_list
