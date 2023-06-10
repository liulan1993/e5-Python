import datetime

def countdown_to_future_date(years):
    current_date = datetime.datetime.now().date()
    future_date = current_date + datetime.timedelta(days=365 * years)
    remaining_time = future_date - current_date

    print(f"从今天到未来 {years} 年后的倒计时开始！")
    print(f"未来日期: {future_date}")
    print(f"剩余时间: {remaining_time.days} 天")

# 设置未来的年数为 1
countdown_to_future_date(1)
