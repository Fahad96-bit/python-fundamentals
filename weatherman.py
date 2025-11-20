import os
import sys


def print_usage():
    print("Usage: weatherman [report#] [data_dir]")
    print()
    print("[Report #]")
    print("1 for Annual Max/Min Temperature")
    print("2 for Hottest day of each year")
    print()
    print("[data_dir]")
    print("Directory containing weather data files")


if len(sys.argv) != 3:
    print_usage()
    sys.exit(1)

report_num = sys.argv[1]
data_dir = sys.argv[2]

if report_num not in ["1", "2"]:
    print_usage()
    sys.exit(1)

if not os.path.isdir(data_dir):
    print_usage()
    sys.exit(1)

if report_num == "1":
    report = {}
    for file in os.listdir(data_dir):
        year = file.split("_")[2]
        with open(f"{data_dir}/{file}") as my_file:
            for line in my_file:
                parts = line.strip().split(",")
                if (
                    parts[0] == "PKT"
                    or parts[0] == "PKST"
                    or parts[0].startswith("<!--")
                    or parts[0] == ""
                ):
                    continue
                if year not in report:
                    report[year] = {
                        "maxTemp": None,
                        "minTemp": None,
                        "maxHumidity": None,
                        "minHumidity": None,
                    }
                if parts[1] != "":
                    report[year]["maxTemp"] = (
                        max(report[year]["maxTemp"], int(parts[1]))
                        if report[year]["maxTemp"] is not None
                        else int(parts[1])
                    )
                if parts[3] != "":
                    report[year]["minTemp"] = (
                        min(report[year]["minTemp"], int(parts[3]))
                        if report[year]["minTemp"] is not None
                        else int(parts[3])
                    )
                if parts[7] != "":
                    report[year]["maxHumidity"] = (
                        max(report[year]["maxHumidity"], int(parts[7]))
                        if report[year]["maxHumidity"] is not None
                        else int(parts[7])
                    )
                if parts[9] != "":
                    report[year]["minHumidity"] = (
                        min(report[year]["minHumidity"], int(parts[9]))
                        if report[year]["minHumidity"] is not None
                        else int(parts[9])
                    )

    print("Year    MAX Temp    MIN Temp    MAX Humidity    MIN Humidity")
    print("-" * 70)
    for year in sorted(report.keys()):
        max_temp = (
            report[year]["maxTemp"] if report[year]["maxTemp"] is not None else "N/A"
        )
        min_temp = (
            report[year]["minTemp"] if report[year]["minTemp"] is not None else "N/A"
        )
        max_humidity = (
            report[year]["maxHumidity"]
            if report[year]["maxHumidity"] is not None
            else "N/A"
        )
        min_humidity = (
            report[year]["minHumidity"]
            if report[year]["minHumidity"] is not None
            else "N/A"
        )
        print(
            f"{year}    {max_temp}       {min_temp}        {max_humidity}         {min_humidity}"
        )

elif report_num == "2":
    report = {}
    for file in os.listdir(data_dir):
        year = file.split("_")[2]
        with open(f"{data_dir}/{file}") as my_file:
            for line in my_file:
                parts = line.strip().split(",")
                if (
                    parts[0] == "PKT"
                    or parts[0] == "PKST"
                    or parts[0].startswith("<!--")
                    or parts[0] == ""
                ):
                    continue
                if year not in report:
                    report[year] = {
                        "date": None,
                        "temp": None,
                    }
                if parts[1] != "":
                    temp = int(parts[1])
                    if report[year]["temp"] is None or temp > report[year]["temp"]:
                        report[year]["temp"] = temp
                        date_parts = parts[0].split("-")
                        if len(date_parts) == 3:
                            report[year][
                                "date"
                            ] = f"{date_parts[2]}/{date_parts[1]}/{date_parts[0]}"

    print("Year    Date       Temp")
    print("-" * 30)
    for year in sorted(report.keys()):
        date = report[year]["date"] if report[year]["date"] is not None else "N/A"
        temp = report[year]["temp"] if report[year]["temp"] is not None else "N/A"
        print(f"{year}    {date}  {temp}")
