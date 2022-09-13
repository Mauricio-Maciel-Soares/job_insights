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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
