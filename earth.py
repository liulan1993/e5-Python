# 地球参数
earth_mass = 5.972 * 10 ** 24  # 地球质量，单位：千克
earth_radius = 6.371 * 10 ** 6  # 地球半径，单位：米

def calculate_gravity_balance(mass, distance):
    # 计算重力平衡参数
    g = (6.67430 * 10 ** -11) * earth_mass / (earth_radius + distance) ** 2  # 重力加速度，单位：米/秒^2
    weight = mass * g  # 物体在该位置的重力，单位：牛顿
    gravity_balance = weight / (mass * 9.8)  # 重力平衡参数，重力与物体重量的比值

    return gravity_balance

# 测试示例
object_mass = 100  # 物体质量，单位：千克
object_distance = 10000  # 物体距离地心的距离，单位：米

balance = calculate_gravity_balance(object_mass, object_distance)
print("重力平衡参数:", balance)
