def protocol_with_differential(steering_command, left_speed_command, right_speed_command):
    return str(steering_command+7).zfill(2) + str(left_speed_command + 255).zfill(3) + str(right_speed_command + 255).zfill(3) + '\n'

def protocol_without_differential(steering_command, speed_command):
    return str(steering_command+7).zfill(2) + str(speed_command + 255).zfill(3) + '\n'