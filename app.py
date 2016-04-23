import weather
import emailer
from settings import VISITORS_STUB_FILE, SCHEDULE_STUB_FILE, CIRCUS_LOCATION


def get_visitors():
    visitors = {}

    try:
        visitors_file = open(VISITORS_STUB_FILE, "r")

        for line in visitors_file:
            (email, name) = line.split(", ")
            visitors[email] = name.strip()

        return visitors

    except FileNotFoundError as err:
        print(err)


def get_schedule():
    try:
        schedule_file = open(SCHEDULE_STUB_FILE, "r")
        schedule = schedule_file.read()
        return schedule
    except FileNotFoundError as err:
        print(err)


def main():
    print("\nWelcome to Circus Emailer App!\n")
    visitors = get_visitors()
    schedule = get_schedule()
    forecast = weather.get_weather_forecast(CIRCUS_LOCATION)
    emailer.send_emails(visitors, schedule, forecast)
    print("\nThank you for using this App. Bye!\n\n")


if __name__ == "__main__":
    main()
