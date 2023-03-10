from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Web developer",
            "min_salary": "invalid",
            "max_salary": "invalid",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": " ",
        },
        {
            "title": "Back end developer",
            "min_salary": " ",
            "max_salary": "3000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
    ]
    criteria = "min_salary"
    result = sort_by(jobs, criteria)
    expected = [
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": " ",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Back end developer",
            "min_salary": " ",
            "max_salary": "3000",
        },
        {
            "title": "Web developer",
            "min_salary": "invalid",
            "max_salary": "invalid",
        },
    ]
    assert result == expected
