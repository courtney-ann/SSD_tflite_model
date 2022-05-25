import smbus
import time
from mpu6050 import mpu6050

mpu=mpu6050(0x68)
prev_x_val = 0
prev_y_val = 0
prev_z_val = 0

prev_g_x = 0
prev_g_y = 0
prev_g_z = 0

accel_data = mpu.get_accel_data()

while (1):
    x_val = accel_data['x']
    y_val = accel_data['y']
    z_val = accel_data['z']

    gyro_data = mpu.get_gyro_data()
    g_x = gyro_data['x']
    g_y = gyro_data['y']
    g_z = gyro_data['z']

    time.sleep(1)

    prev_x_val = x_val
    prev_y_val = y_val
    prev_z_val = z_val

    prev_g_x = g_x
    prev_g_y = g_y
    prev_g_z = g_z

    a_x_diff = x_val - prev_x_val
    g_x_diff = g_x - prev_g_x
    g_y_diff = g_y - prev_g_y
    g_z_diff = g_z - prev_g_z

    result1 = str(x_val)
    result2 = str(g_x)
    result3 = str(g_y)
    result4 = str(g_y)
    result5 = str(mpu.get_temp())
    result6 = str(y_val)
    result7 = str(z_val)
    print(f"x: {result1}")
    print(f"y: {result6}")
    print(f"z: {result7}")
    print(f"gx: {result2}")
    print(f"gy: {result3}")
    print(f"gz: {result4}")
    print(f"temp: {result5}")











