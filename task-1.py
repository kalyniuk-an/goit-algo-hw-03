from datetime import datetime

def get_days_from_today(date):
  try:
    input_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()
    difference = input_date.date() - current_date.date()
    return difference.days
  except ValueError:
    return f"Invalid date format '{date}'. Expected format: 'YYYY-MM-DD'."
  
date = "2026-03-14"
print(get_days_from_today(date))