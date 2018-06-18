from fetch_attendance import Fetch_attend

attend = Fetch_attend('ogawa',2018,5,160,150)
print(attend.first_day())
print(attend.last_day())
print(attend.total_workdays())
print(attend.molcure_attendance())
attend_list, a_type= attend.molcure_attendance()
print(a_type)
print(attend.nedo_attendance())
