import os
import sys
import argparse
from datetime import datetime

TEMPERATURE_REPORT = "1"
HOTTEST_DAY_REPORT = "2"


def print_usage():
    print("Usage: weatherman [report#] [data_dir]")
    print()
    print("[Report #]")
    print(f"{TEMPERATURE_REPORT} for Annual Max/Min Temperature")
    print(f"{HOTTEST_DAY_REPORT} for Hottest day of each year")
    print()
    print("[data_dir]")
    print("Directory containing weather data files")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Weather data analysis tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "report_num",
        type=str,
        choices=[TEMPERATURE_REPORT, HOTTEST_DAY_REPORT],
    )
    parser.add_argument(
        "data_dir",
        type=str,
    )

    try:
        return parser.parse_args()
    except SystemExit:
        print_usage()
        sys.exit(1)


def validate_directory(dir_path):
    if not os.path.isdir(dir_path):
        raise argparse.ArgumentTypeError(f"Directory does not exist: {dir_path}")

    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

    if not files:
        raise argparse.ArgumentTypeError(f"Directory is empty: {dir_path}")

    text_files = [f for f in files if f.endswith(".txt")]
    if not text_files:
        raise argparse.ArgumentTypeError(f"No text files found in directory: {dir_path}")

    return True


def is_valid_line(parts):
    return not (parts[0] == "PKT" or parts[0] == "PKST" or parts[0].startswith("<!--") or parts[0] == "")


def parse_weather_files(data_dir):
    weather_data = []

    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        if not os.path.isfile(file_path) or not file.endswith(".txt"):
            continue

        try:
            year = file.split("_")[2]
        except IndexError:
            continue

        with open(file_path, "r") as my_file:
            for line in my_file:
                parts = line.strip().split(",")

                if not is_valid_line(parts):
                    continue

                weather_data.append(
                    {
                        "year": year,
                        "date": parts[0],
                        "max_temp": parts[1] if len(parts) > 1 else "",
                        "min_temp": parts[3] if len(parts) > 3 else "",
                        "max_humidity": parts[7] if len(parts) > 7 else "",
                        "min_humidity": parts[9] if len(parts) > 9 else "",
                    }
                )
    return weather_data


def extract_report_1(weather_data):
    report = {}

    field_config = {
        "max_temp": {"func": max},
        "min_temp": {"func": min},
        "max_humidity": {"func": max},
        "min_humidity": {"func": min},
    }

    for data in weather_data:
        year = data["year"]

        if year not in report:
            report[year] = {
                "max_temp": None,
                "min_temp": None,
                "max_humidity": None,
                "min_humidity": None,
            }
        for field_name, config in field_config.items():
            value_str = data[field_name]
            if value_str != "":
                try:
                    value = int(value_str)
                    current = report[year][field_name]
                    if current is None:
                        report[year][field_name] = value
                    else:
                        report[year][field_name] = config["func"](current, value)
                except ValueError:
                    continue

    for year in report:
        for field in report[year]:
            if report[year][field] is None:
                report[year][field] = "N/A"

    return report


def extract_report_2(weather_data):
    report = {}

    for data in weather_data:
        year = data["year"]

        if year not in report:
            report[year] = {
                "date": None,
                "temp": None,
            }

        max_temp_str = data["max_temp"]
        if max_temp_str != "":
            try:
                temp = int(max_temp_str)
                current_temp = report[year]["temp"]

                if current_temp is None or temp > current_temp:
                    report[year]["temp"] = temp
                    date_obj = datetime.strptime(data["date"], "%Y-%m-%d")
                    report[year]["date"] = date_obj.strftime("%d/%m/%Y")
            except ValueError:
                continue

    for year in report:
        if report[year]["date"] is None:
            report[year]["date"] = "N/A"
        if report[year]["temp"] is None:
            report[year]["temp"] = "N/A"

    return report


def display_report_1(report):
    print("Year    MAX Temp    MIN Temp    MAX Humidity    MIN Humidity")
    print("-" * 70)
    for year in sorted(report.keys()):
        max_temp = report[year]["max_temp"]
        min_temp = report[year]["min_temp"]
        max_humidity = report[year]["max_humidity"]
        min_humidity = report[year]["min_humidity"]
        print(f"{year}    {max_temp}       {min_temp}        {max_humidity}         {min_humidity}")


def display_report_2(report):
    print("Year    Date       Temp")
    print("-" * 30)
    for year in sorted(report.keys()):
        date = report[year]["date"]
        temp = report[year]["temp"]
        print(f"{year}    {date}  {temp}")


def main():
    try:
        args = parse_arguments()
        validate_directory(args.data_dir)

        weather_data = parse_weather_files(args.data_dir)

        if not weather_data:
            print("No valid weather data found in the directory.")
            sys.exit(1)

        if args.report_num == TEMPERATURE_REPORT:
            report = extract_report_1(weather_data)
            display_report_1(report)
        elif args.report_num == HOTTEST_DAY_REPORT:
            report = extract_report_2(weather_data)
            display_report_2(report)

    except argparse.ArgumentTypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
