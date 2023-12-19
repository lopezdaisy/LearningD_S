text = 'ice cream'
print(text)
print(text[2])
print(text[0:3])
print(text[4:])
print("Let's learn Python")
address = '''1 Purple Street
Kisumu
Kenya'''
print(address)
s1 = 'Hello'
s2 = 'World'
print(s1 +" "+ s2)
num = 254
print(s1 +" "+ s2 +" " + str(num))

from datetime import datetime, timedelta
import re

def convert_time(time_str, start_zone, end_zone):
    # Define time zones and their UTC offsets
    time_zones = {'Eastern': -5, 'Central': -6, 'Mountain': -7, 'Pacific': -8}

    # Convert time_str to a datetime object
    time_format = "%I:%M%p"
    time_object = datetime.strptime(time_str, time_format)

    # Calculate the time difference in hours
    time_difference = time_zones[end_zone] - time_zones[start_zone]

    # Apply the time difference
    converted_time = time_object + timedelta(hours=time_difference)

    # Format the result
    result_str = converted_time.strftime(time_format)

    return result_str

# Example usage:
time_input = input("Enter the time (e.g., 3:48pm): ")
start_zone_input = input("Enter the starting time zone (Eastern, Central, Mountain, or Pacific): ")
end_zone_input = input("Enter the ending time zone (Eastern, Central, Mountain, or Pacific): ")

# Validate the time format using regular expression
time_pattern = re.compile(r'^\d{1,2}:\d{2}(am|pm)$')
if not time_pattern.match(time_input.lower()):
    print("Invalid time format. Please enter the time in the format like 3:48pm.")
else:
    # Validate time zone inputs
    valid_time_zones = ['Eastern', 'Central', 'Mountain', 'Pacific']
    if start_zone_input not in valid_time_zones or end_zone_input not in valid_time_zones:
        print("Invalid time zone. Please enter a valid time zone.")
    else:
        converted_time = convert_time(time_input, start_zone_input, end_zone_input)
        print(f"The converted time is: {converted_time}")
