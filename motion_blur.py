#%%
class DroneCamera:
    def __init__(self, sensor_width, sensor_height, pixel_pitch, focal_length, fastest_shutter_speed):
        self.sensor_width = sensor_width # in millimeters
        self.sensor_height = sensor_height # in millimeters
        self.pixel_pitch = pixel_pitch # in micrometers
        self.focal_length = focal_length # in millimeters
        self.fastest_shutter_speed = fastest_shutter_speed # in seconds
    
    def calculate_gsd(self, altitude):
        gsd = (self.focal_length * self.pixel_pitch * altitude) / (self.sensor_width * 1000)
        return gsd
    
    def calculate_motion_blur(self, altitude, speed):
        gsd = self.calculate_gsd(altitude)
        motion_blur = (self.pixel_pitch * altitude * speed * (self.focal_length / (self.focal_length**2 + self.sensor_width**2 + self.sensor_height**2)**0.5)) / (self.fastest_shutter_speed * 1000)
        if motion_blur > gsd:
            print("Warning: Motion blur is greater than 1x GSD.")
        return motion_blur


#%%
# create a DroneCamera object
camera = DroneCamera(sensor_width=6.2, sensor_height=4.6, pixel_pitch=1.4, focal_length=50, fastest_shutter_speed=1/8000)

# calculate GSD for altitude of 100 meters
gsd = camera.calculate_gsd(100)
print(f"GSD: {gsd} meters/pixel")

# calculate motion blur for altitude of 100 meters and speed of 10 m/s
motion_blur = camera.calculate_motion_blur(100, 10)
print(f"Motion blur: {motion_blur} meters")

# %%
