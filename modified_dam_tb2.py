"""modified_dam_tb2.py"""

import os
import csv


def extractor():
    """extrctor"""
    dir = os.path.dirname(os.path.abspath(__file__))
    task = os.path.join(dir, "task_1.csv")

    with open(task, "r", encoding="utf-8-sig") as task:
        task_read = list(csv.DictReader(task))
    return task_read


def filter(n):
    """filter"""
    task_data = extractor()
    dam_hour_list = [
        {"date": row["date"].split(" ")[0], "dam": row["dam"]}
        for row in task_data
        if row["date"].startswith(n)
    ]

    tbn_list = []
    for _ in range(0, 2):
        max_entry = max(dam_hour_list, key=lambda x: float(x["dam"]))
        min_entry = min(dam_hour_list, key=lambda x: float(x["dam"]))
        tbn_list.append(max_entry)
        tbn_list.append(min_entry)
        dam_hour_list.remove(max_entry)
        dam_hour_list.remove(min_entry)

    max_dam = float(tbn_list[0]["dam"]) + float(tbn_list[2]["dam"])
    min_dam = float(tbn_list[1]["dam"]) + float(tbn_list[3]["dam"])
    result = round(max_dam - min_dam, 2)
    return result


def tbn_revenue():
    """
    tbn_revenue
    """
    data = extractor()
    unique_dates = sorted(list(set(row["date"].split(" ")[0] for row in data)))
    final_result = {i: filter(i) for i in unique_dates}

    with open(
        "modified_dam_tb2.csv", "w", newline="", encoding="utf-8-sig"
    ) as csv_file:
        fieldnames = ["date", "tb2"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(
            [
                {"date": date, "tb2": tb2_value}
                for date, tb2_value in final_result.items()
            ]
        )


if __name__ == "__main__":
    print(tbn_revenue())
