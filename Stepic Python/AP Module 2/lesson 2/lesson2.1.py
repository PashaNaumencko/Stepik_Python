import datetime
data_in = input().split()
result_date = datetime.date(int(data_in[0]), int(data_in[1]), int(data_in[2])) + datetime.timedelta(days=int(input()))
print(result_date.year, result_date.month, result_date.day)
