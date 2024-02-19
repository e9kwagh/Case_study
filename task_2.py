"""task_01"""
import csv
import os
from datetime import datetime


def rtm():
    """rtm
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    Rtm = os.path.join(dir, "RTM_Prices_2022.csv")

    with open(Rtm, "r", encoding="utf-8-sig") as Rtm:
        rtm_read = csv.DictReader(Rtm)
        hb_north = [row for row in rtm_read if row["Settlement Point"] == "HB_NORTH"]
        return hb_north


def dam():
    """dam
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    Dam = os.path.join(dir, "DAM_Prices_2022.csv")

    with open(Dam, "r", encoding="utf-8-sig") as Dam:
        rtm_read = csv.DictReader(Dam)
        hb_north = [row for row in rtm_read if row["Settlement Point"] == "HB_NORTH"]
        return hb_north


def solution():
    """solution
    """
    hb_north_rtm = rtm()
    hb_north_dam = dam()

    rtm_val = [float(i["Settlement Point Price"]) for i in hb_north_rtm]
    rtm_prices = [round(price, 2) for price in rtm_val]

    dam_prices = {
        f"{row['Delivery Date']} {int(row['Delivery Hour']) - 1}": float(
            row["Settlement Point Price"]
        )
        for row in hb_north_dam
    }
    output_data = []

    for datetime_key in dam_prices.keys():
        dam_price = round(dam_prices[datetime_key], 2)
        rtm_price = rtm_prices.pop(0)
        output_data.append(
            {
                "date": datetime.strptime(datetime_key, "%m/%d/%Y %H").strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "dam": dam_price,
                "rtm": rtm_price,
            }
        )

    with open("task_2.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
        fieldnames = ["date", "dam", "rtm"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)


if __name__ == "__main__":
    solution()
