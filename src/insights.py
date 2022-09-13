from src.jobs import read


def get_unique_job_types(path):
    content = read(path)
    job_types = set()
    for index in content:
        job_type = index["job_type"]
        if job_type not in job_types:
            job_types.add(job_type)

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_list = []
    for index in jobs:
        filtered_job = index["job_type"]
        if filtered_job == job_type:
            filtered_list.append(index)
    return filtered_list


def get_unique_industries(path):
    content = read(path)
    industries_list = set()

    for index in content:
        industries = index["industry"]
        if industries != '':
            industries_list.add(industries)

    return industries_list


def filter_by_industry(jobs, industry):
    filtered_list = []
    for index in jobs:
        filtered_job = index["industry"]
        if filtered_job == industry:
            filtered_list.append(index)
    return filtered_list


def get_max_salary(path):
    content = read(path)
    max_salary = []
    for index in content:
        if index["max_salary"].isnumeric():
            max_salary.append(int(index["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    content = read(path)
    min_salary = []
    for index in content:
        if index["min_salary"].isnumeric():
            min_salary.append(int(index["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("doesn't exists")

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("aren't valid integers")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can't be greather than max_salary")

    if type(salary) != int:
        raise ValueError("isn't a valid integer")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
