import datetime as dt
import pandas as pd
from pandas.tseries.holiday import ( Holiday, USMartinLutherKingJr, USMemorialDay, USLaborDay, USThanksgivingDay,
    nearest_workday, previous_friday, next_monday)
from dateutil.relativedelta import FR

# ->> Recognized org holidays and workday observances (if applicable)
new_years = Holiday('New Years Day', month=1, day=1, observance=nearest_workday)
mlk_jr = USMartinLutherKingJr
memorial = USMemorialDay
independence = Holiday('Independence Day', month=7, day=4, observance=nearest_workday)
labor = USLaborDay
thxgiving = USThanksgivingDay
after_thxgiving = Holiday('Day after Thanksgiving', month=11, day=1, offset=pd.DateOffset(weekday=FR(4)))
christmas_eve = Holiday('Christmas Eve', month=12, day=24, observance=previous_friday)
christmas = Holiday('Christmas', month=12, day=25, observance=next_monday)
holidays = [new_years, mlk_jr, memorial, independence, labor, thxgiving, after_thxgiving, christmas_eve, christmas]

def date_table_holidays(holiday_list, start, end) -> pd.DataFrame:
    holiday_series = pd.concat([pd.Series(h.dates(start, end)) for h in holiday_list])
    dates = pd.date_range(start, end)
    df = pd.DataFrame({'date': dates})
    df['holiday'] = df['date'].isin(holiday_series)
    return df
    
s = dt.date(2012, 1, 1) # ->> start date for testing
e = dt.date(2022, 12, 31) # ->> end date
df = date_table_holidays(holidays, s, e)
df.to_excel('holiday_date_table.xlsx', index=None)
