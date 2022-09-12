from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for job_title in content:
            jobs_list.append(job_title)
    return jobs_list
