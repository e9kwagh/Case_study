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
    li = [ i["dam"].strip()  for i in  dam_hour_list]
    li = [float(item) for item in li]
    print("li =", li)
    
    
# def tdn_list():
#     result= []
#     dates = date()
#     for i in dates : 
#        result.append(filter(i))
#     return result


    max_diff = 0
    max_val = None
    min_val = None

    for i in range(1, len(li)):
        min_price = min(li[:i])
       
        current_diff = li[i] - min_price
        if current_diff > max_diff:
            max_diff = current_diff
            max_val = li[i]
            min_val = min_price
        print(max_val)
    
    li.remove(max_val)
    li.remove(min_val)

    return round(max_diff, 2)


def modified_tbn(date):
    ans=[]
    for _ in range(2): 
        val = filter(date)     
        ans.append(val)
        
    return sum(ans)



def date():
    data = extractor()
    val= set()
    for i in data:
        val.add(i["date"].split(" ")[0])
    date= list(val)
    date_list = sorted(date)
    return date_list

def tbn_revenue():
    """
    tbn_revenue
    """
    # data = extractor()
    dates = date()

    final_result = {date: modified_tbn(date) for date in dates}

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
   
    # data = filter("2022-01-01")
    # print(modified_tbn(data))
    # print(date())
    # print(modified_tbn("2022-01-01") , " = modified_tbn")
    # print(filter("2022-01-01"))
    # print(tbn_revenue())
    