"""TBn_revenue.py
"""

import os
import csv


def task_1(n):
    """task_1"""
    dir = os.path.dirname(os.path.abspath(__file__))
    task = os.path.join(dir, "task_1.csv")

    with open(task, "r", encoding="utf-8-sig") as task:
        task_read = list(csv.DictReader(task))

        task_dam = [
            {
                "date": row["date"].split(" ")[0],
                "dam": row["rtm"],
            }
            for row in task_read
            if row["date"].startswith(n)
        ]

        unique_dates = sorted(list(set(row["date"].split(" ")[0] for row in task_read)))
        return (task_dam, unique_dates)


def tbn_revenue(data, n):
    """tbn_revenue"""
    sum_start, sum_end = 0, 0
    for i in range(0, n):
        sum_start += float(data[i]["dam"])
        sum_end += float(data[-(i + 1)]["dam"])
    return round(sum_start - sum_end, 2)


def solution_dam():
    """
    solution_dam
    """
    dates = task_1("2022-01-01")[1]
    revenue = {}
    for date in dates:
        task_dam = task_1(date)[0]
        sort_dam = sorted(task_dam, key=lambda x: float(x["dam"]), reverse=True)
        revenue[date] = tbn_revenue(sort_dam, 2)
    return revenue


def dam_tb2():
    """dam_tb2"""
    results = solution_dam()
    with open("rtm_tb2.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
        fieldnames = ["date", "rtm_price"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(
            [
                {"date": date, "rtm_price": tb2_value}
                for date, tb2_value in results.items()
            ]
        )


if __name__ == "__main__":
    print(dam_tb2())
    # print(task_1())
