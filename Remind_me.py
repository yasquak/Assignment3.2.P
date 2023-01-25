def remind_me():
    from datetime import date

    today = date.today()
    date_today = today.strftime("%d/%m")

    important_dates = {
      "12/01": "My birthday",
      "25/01": "Programming day",
      "26/01": "Birthday A. H.",
      "05/02": "Birthday B. P.",
      "12/02": "Birthday A. S.",
      "01/03": "Birthday F. K.",
      "21/12": "Birthday V. L.",
    }

    if date_today in important_dates:
        print(date_today, important_dates[date_today])
