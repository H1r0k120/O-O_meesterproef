import pandas as pd
import datetime
from datetime import date
from zermelo import Client

def get_tabledata(atoken):

    today = date.today()

    # Example Usage
    sdate_input = today.strftime("%Y-%m-%d")  # Example date
    stime_input = "00:00:00"    # Example time (optional, defaults to midnight)

    edate_input = today.strftime("%Y-%m-%d")
    etime_input = "23:59:59"

    # Function to convert readable time to Unix timestamp
    def to_unix_timestamp(date_string, time_string="00:00:00"):
        """Converts a given date and time string to a Unix timestamp."""
        dt = datetime.datetime.strptime(f"{date_string} {time_string}", "%Y-%m-%d %H:%M:%S")
        unix_timestamp = int(dt.timestamp())
        return unix_timestamp

    start_utime = to_unix_timestamp(sdate_input, stime_input)
    end_utime = to_unix_timestamp(edate_input, etime_input)

    # Initialize Zermelo Client
    cl = Client("keizerkarelcollege")

    # Fetch appointments
    #atoken = "nrodnludj19gqmdtehi3ueiufm"
    appointments = cl.get_appointments(atoken, start_utime, end_utime)

    # Extract relevant data
    schedule_data = []
    for appointment in appointments["response"]["data"]:
        start_time = datetime.datetime.fromtimestamp(appointment["start"]).strftime("%H:%M")
        end_time = datetime.datetime.fromtimestamp(appointment["end"]).strftime("%H:%M")
        #date = datetime.datetime.fromtimestamp(appointment["start"]).strftime("%Y-%m-%d")
        
        # Extract subject, teacher, and location (handle missing values)
        subject = ", ".join(appointment.get("subjects", ["Unknown"]))
        teacher = ", ".join(appointment.get("teachers", ["Unknown"]))
        location = ", ".join(appointment.get("locations", ["Unknown"]))

        # Append to schedule list
        schedule_data.append([start_time, end_time, subject, teacher, location])

    # Convert to DataFrame
    df = pd.DataFrame(schedule_data, columns=["Start Time", "End Time", "Subject", "Teacher", "Location"])

    #df["Sort Time"] = pd.to_datetime(df["Start Time"])  # Combine Date & Start Time
    df["Sort Time"] = pd.to_datetime(today.strftime("%Y-%m-%d") + " " + df["Start Time"], format="%Y-%m-%d %H:%M")
    df = df.sort_values(by=["Sort Time"]).drop(columns=["Sort Time"]).reset_index(drop=True)  # Sort & remove helper column

    # Return the timetable
    
    if df.empty:
        return "No appointments found."
    else:
        return df
    
#print(get_tabledata('39jb2e0ab209d41vvgt9782fca'))