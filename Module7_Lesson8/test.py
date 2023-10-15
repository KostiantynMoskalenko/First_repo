from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)   # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)   # 2019-12-10 14:00:00