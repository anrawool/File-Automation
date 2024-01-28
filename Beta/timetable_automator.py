import __meta
import helpers
import calendar_manager
import datetime
import re


calendar_instance = calendar_manager.CalendarInstance("../credentials.json")
data = helpers.fetch_timetable()
data = data.to_dict("list")
data = list(zip(data["Date"], data["Class 1"], data["Class 2"]))
for index, item in enumerate(data):
    data[index] = list(item)
    data[index][0] = data[index][0].replace("(", "")
    data[index][0] = data[index][0].replace(")", "")
    data[index][0] = datetime.datetime.strptime(data[index][0], "%d/%m/%Y").strftime(
        "%Y-%m-%d"
    )
    if data[index][1] != "-":
        time = re.search(r"\d\d:\d\d-\d\d:\d\d", data[index][1])
        time = time.group(0)
        start, stop = time.split("-")
        starttime = datetime.datetime.strptime(start, "%H:%M")
        starttime = datetime.datetime.strftime(starttime, "%H:%M:%S")
        timeend = datetime.datetime.strptime(stop, "%H:%M")
        timeend = datetime.datetime.strftime(timeend, "%H:%M:%S")
        print(starttime)
        print(timeend)
        data[index][1] = data[index][1].replace(time, "")
        print(time)

print(timeend)
#     else:
#         continue
# print(data)
