def add_time(start, duration, day = ""):
    start_components = start.split(" ")
    start_parts = start_components[0].split(":")
    period = start_components[1]
    start_hour = int(start_parts[0]) + 12 if period == "PM" else int(start_parts[0])
    start_minutes = 60*start_hour + int(start_parts[1])

    duration_parts = duration.split(":")
    duration_minutes = int(duration_parts[0]) * 60 + int(duration_parts[1])
    new_minutes_total = start_minutes + duration_minutes
    new_day = new_minutes_total // (60 * 24)
    new_hour = (new_minutes_total - new_day * 60 * 24) // 60
    new_minutes = new_minutes_total - new_hour * 60 - new_day * 60 * 24
    afternoon = True if new_minutes_total - new_day * 60 * 24 >= 60 * 12 else False

    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    day_num = days.index(day.lower()) if day != "" else None
    new_day_num = (day_num + new_day) % 7 if day != "" else None
    new_day_str = (days[new_day_num]).title() if day != "" else None

    day_comment = f" ({str(new_day)} days later)" if new_day > 1 else f" (next day)"

    new_time = (str(new_hour - 12*afternoon) if new_hour - 12*afternoon != 0 else "12") + ":" + (str(new_minutes) if new_minutes >= 10 else f"0{new_minutes}") + (" PM" if afternoon else " AM") + (f", {new_day_str}" if day != "" else "") + (day_comment if new_day > 0 else "")
    
    return new_time

print(add_time("11:59 AM", "24:05"))