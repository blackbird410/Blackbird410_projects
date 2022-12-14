#!\bin\env python

def add_time(current_time, time_to_add, start_day=""):
    days = {"Monday":1,
            "Tuesday":2,
            "Wednesday":3,
            "Thursday":4,
            "Friday":5,
            "Saturday":6,
            "Sunday":7
            }
    if start_day:
        start_day = start_day[0].upper() + start_day[1:].lower()

    n_day = 0

    l1 = current_time.split(" ")
    l1[0] = l1[0].split(":")
    
    l2 = time_to_add.split(":")

    mns = int(l1[0][1]) + int(l2[1])
    hrs = int(l1[0][0]) + int(l2[0])

    if l1[1] == "PM":
        hrs += mns // 60 + 12
    else:
        hrs += mns // 60

    n_day = hrs // 24
    mns = mns % 60
    hrs = hrs % 24

    if len(str(mns)) < 2:
        mns = "0" + str(mns)

    if not n_day:
        if hrs == 12:
            if start_day:
                return f"{hrs}:{mns} PM, {start_day}"
            else:
                return f"{hrs}:{mns} PM"
        elif hrs > 12:
            if start_day:
                return f"{hrs-12}:{mns} PM, {start_day}"
            else:
                return f"{hrs-12}:{mns} PM"
        else:
            if start_day:
                return f"{hrs}:{mns} AM, {start_day}"
            else:
                return f"{hrs}:{mns} AM"
    else:
        if n_day == 1:
          if not start_day:
            if hrs == 12:
              return f"{hrs}:{mns} AM (next day)"
            elif hrs > 12:
                return f"{hrs-12}:{mns} PM (next day)"
            else:
                return f"{hrs}:{mns} AM (next day)"
          else:
            l = list(days.keys())
            n = days[start_day]
            if hrs == 12:
              return f"{hrs}:{mns} AM, {l[n]} (next day)"
            elif hrs > 12:
                return f"{hrs-12}:{mns}, PM {l[n]} (next day)"
            else:
                return f"{hrs}:{mns} AM, {l[n]} (next day)"
        else:
            if start_day:
                c_day = days[start_day] + (n_day % 7)
                if c_day > 7:
                    c_day -= 7
                for x,y in days.items():
                    if y == c_day:
                        if hrs == 12:
                            return f"{hrs}:{mns} PM, {x} ({n_day} days later)"
                        elif hrs > 12:
                            return f"{hrs-12}:{mns} PM, {x} ({n_day} days later)"
                        else:
                            if hrs == 0:
                                return f"12:{mns} AM, {x} ({n_day} days later)"
                            else:
                                return f"{hrs}:{mns} AM, {x} ({n_day} days later)"
            else:
              if hrs == 12:
                return f"12:{mns} PM ({n_day} days later)"
              elif hrs > 12:
                return f"{hrs-12}:{mns} PM ({n_day} days later)"
              else:
                if hrs == 0:
                  return f"12:{mns} AM ({n_day} days later)"
                else:
                  return f"{hrs}:{mns} AM ({n_day} days later)"


print(add_time("8:16 PM", "466:02", "tuesday"))
