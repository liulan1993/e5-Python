from datetime import datetime

class Vehicle:
    def __init__(self, plate_number):
        self.plate_number = plate_number
        self.out_time = None
        self.in_time = None

    def check_out(self):
        self.out_time = datetime.now()

    def check_in(self):
        self.in_time = datetime.now()

    def get_total_time(self):
        if self.out_time and self.in_time:
            duration = self.in_time - self.out_time
            return duration.total_seconds() / 60  # 返回分钟数
        return 0

# 创建车辆对象
vehicle1 = Vehicle("车辆1")
vehicle2 = Vehicle("车辆2")
vehicle3 = Vehicle("车辆3")

# 车辆出库入库统计
vehicle1.check_out()
vehicle1.check_in()

vehicle2.check_out()
vehicle2.check_in()

vehicle3.check_out()
# 车辆3没有入库记录

# 统计总时间
total_time_vehicle1 = vehicle1.get_total_time()
total_time_vehicle2 = vehicle2.get_total_time()
total_time_vehicle3 = vehicle3.get_total_time()

print(f"车辆1出入库时间总计: {total_time_vehicle1}分钟")
print(f"车辆2出入库时间总计: {total_time_vehicle2}分钟")
print(f"车辆3出入库时间总计: {total_time_vehicle3}分钟")
