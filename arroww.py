# it is thired party library for use time stamp and timezone change


import arrow



utc_tm=arrow.utcnow()
print(utc_tm)

loacl_time=arrow.now()
print("local time",loacl_time)