#!/usr/bin/python3

# # <xbar.title>Datetime</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Cabin Zhu</xbar.author>
# <xbar.author.github>cabinz</xbar.author.github>
# <xbar.desc>A datetime display with a mini drop-down calendar.</xbar.desc>
# <xbar.image></xbar.image>
# <xbar.dependencies>python</xbar.dependencies>
# <xbar.abouturl>https://github.com/cabinz/xbar-datetimecal</xbar.abouturl>
# <xbar.var>string(VAR_DATETIME_FORMAT='%m-%d %a %H:%M'): Format of the datetime displayed in the menu bar.</xbar.var>
# <xbar.var>string(VAR_CALENDAR_COLOR='red'): Color of the current month drop-down calendar.</xbar.var>
# <xbar.var>string(VAR_FONT='Monaco'): Display font in the pop-up menu.</xbar.var>
# <xbar.var>string(VAR_FONT_SIZE=15): Display font size in the pop-up menu.</xbar.var>


import calendar
from datetime import datetime, timedelta
import os

DT_DISP_FMT = os.environ.get("VAR_DATETIME_FORMAT", "%m-%d %a %H:%M")
# DT_DISP_FMT = os.environ.get("VAR_DISPLAY_FORMAT", "%m-%d %a %H:%M:%S") # w/ second
CAL_COLOR = os.environ.get("VAR_CALENDAR_COLOR", "red")
FONT = os.environ.get("VAR_FONT", "Monaco")
FONT_SIZ = int(os.environ.get("VAR_FONT_SIZE", "15"))


def format_calendar(year, month, font, color=None):
    cal = calendar.month(year, month).splitlines()
    formatted_cal = []
    for line in cal:
        if line.strip():
            if color:
                formatted_cal.append(
                    f" {line}|trim=false font={font} size={FONT_SIZ} color={color}"
                )
            else:
                formatted_cal.append(f"--{line}|trim=false font={font} size={FONT_SIZ}")
    return formatted_cal


def main():
    current_time = datetime.now()

    # Display current time
    print(current_time.strftime(DT_DISP_FMT))
    print("---")

    # Display previous month calendar
    prev_month_date = current_time - timedelta(days=current_time.day)
    print(f"Prev: {prev_month_date.strftime('%b %Y')}|trim=false font={FONT}")
    print("\n".join(format_calendar(prev_month_date.year, prev_month_date.month, FONT)))

    print("---")

    # Display current month calendar
    print(
        "\n".join(
            format_calendar(current_time.year, current_time.month, FONT, CAL_COLOR)
        )
    )

    print("---")

    # Display next month calendar
    next_month_date = current_time + timedelta(
        days=(
            calendar.monthrange(current_time.year, current_time.month)[1]
            - current_time.day
            + 1
        )
    )
    print(f"Next: {next_month_date.strftime('%b %Y')}|trim=false font={FONT}")
    print("\n".join(format_calendar(next_month_date.year, next_month_date.month, FONT)))


if __name__ == "__main__":
    main()
