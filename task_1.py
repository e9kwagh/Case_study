"""task_01"""

import csv
import os
from datetime import datetime, timedelta


def rtm():
    """
    rtm
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    Rtm = os.path.join(dir, "RTM_Prices_2022.csv")

    with open(Rtm, "r", encoding="utf-8-sig") as Rtm:
        rtm_read = csv.DictReader(Rtm)
        hb_north = [row for row in rtm_read if row["Settlement Point"] == "HB_NORTH"]
        return hb_north


def dam():
    """
    dam
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    Dam = os.path.join(dir, "DAM_Prices_2022.csv")

    with open(Dam, "r", encoding="utf-8-sig") as Dam:
        rtm_read = csv.DictReader(Dam)
        hb_north = [row for row in rtm_read if row["Settlement Point"] == "HB_NORTH"]
        return hb_north


def solution():
    """solution"""
    hb_north_rtm = rtm()
    hb_north_dam = dam()

    rtm_val = [float(i["Settlement Point Price"]) for i in hb_north_rtm]
    rtm_list = []

    for i in range(0, len(rtm_val), 4):
        group = rtm_val[i : i + 4]
        average = sum(group) / len(group)
        rtm_list.append(round(average, 2))

    rtm_prices = rtm_list
    dam_prices = {
        f"{row['Delivery Date']} {int(row['Delivery Hour']) - 1}": float(
            row["Settlement Point Price"]
        )
        for row in hb_north_dam
    }

    output_data = []
    for i, rtm_price in enumerate(rtm_prices):
        datetime_key = list(dam_prices.keys())[i]
        dam_price = dam_prices.get(datetime_key, 0.0)
        output_data.append(
            {
                "date": datetime.strptime(datetime_key, "%m/%d/%Y %H").strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "dam": round(dam_price, 2),
                "rtm": round(rtm_price, 2),
            }
        )

    with open("task_1.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
        fieldnames = ["date", "dam", "rtm"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)


if __name__ == "__main__":
    solution()

    # for row in reader:
    #     print(row)

    # start_date = datetime(2022, 1, 1)
    # end_date =  datetime(2022, 1, 31, 23)

# for i in range(0, len(hb_north_rtm), 4):
#
#

# hb_north_rtm_hourly = [i for i in hb_north_rtm if int(i["Delivery Interval"]) == 1]


#         hb_north = []
#         rtm_hour_price = [  i  for i in range(len(hb_north),4)  ]
#         print(rtm_hour_price)


# how can i take out avg of every Settlement Point Price  after every of every  in  hb_north


# with open(Dam, "r", encoding="utf-8") as Dam:
#     dam_file  = Dam.readlines()

# with open(Rtm,"r" ,encoding="utf-8") as Rtm:
#     rtf_file  = Rtm.readlines()

# dam_list =  [i   for i in dam_file if "HB_HOUSTON" in i  ]
# rtf_file =  [i.split(",")  for i in dam_file if "HB_HOUSTON" in i]

#


# hb_houstan = [ i  for i in reader if "HB_HOUSTON" in  i  ]
# print("hb_houstan",= hb_houstan )
# return hb_houstan


# li = []
# dam_avg = {i : li.append(rtf_file["Settlement Point Price"])  for i in range(1,25) if  rtf_file["Delivery Hour"] == i    }
# dam_price = { row[1] : row[3]   for row in dam_list   }

# print("dam_list = ",dam_list)
# print(dam_list)


# def read_data(Dam):
#         data = {}
#         with open(Dam, 'r') as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
#                 date, hour, sp, price = row
#                 if sp == 52.82:
#                     datetime_str = f'{date} {hour}:00:00'
#                     data[datetime_str] = float(price)
#         return data


# with open('task_1.csv', 'w', newline='') as result_file:
#     result_file.write('date,dam,rtm\n')
#     for row in result_list:
#         result_file.write(','.join(map(str, row)) + '\n')
