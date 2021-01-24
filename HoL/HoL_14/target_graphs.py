from csv import DictReader
from datetime import datetime

convert_bool = lambda str_val: True if str_val == "TRUE" else False

targets = []
with open("/home/cloud_user/target.csv", newline="") as f:
    reader = DictReader(f)
    for row in reader:
        try:
            row["AllCapability"] = eval(row["AllCapability"])
        except SyntaxError:
            # This happens if the field is an empty string instead of a list
            row["AllCapability"] = []

        row["Is24Hours.MF"] = convert_bool(row["Is24Hours.MF"])
        row["Is24Hours.Sat"] = convert_bool(row["Is24Hours.Sat"])
        row["Is24Hours.Sun"] = convert_bool(row["Is24Hours.Sun"])
        row["IsOpen.MF"] = convert_bool(row["IsOpen.MF"])
        row["IsOpen.Sat"] = convert_bool(row["IsOpen.Sat"])
        row["IsOpen.Sun"] = convert_bool(row["IsOpen.Sun"])
        row["LocationMilestones.OpenDate"] = datetime.strptime(
            row["LocationMilestones.OpenDate"], "%Y-%m-%dT%H:%M:%S"
        )
        targets.append(row)

# Example dictionary in targets
# {
#   "X.locale": "en-US",
#   "Address.AddressLine1": "400 Oxford Exchange Blvd",
#   "Address.AddressLine2": "",
#   "Address.City": "Oxford",
#   "Address.CountryName": "United States",
#   "Address.County": "Calhoun",
#   "Address.FormattedAddress": "400 Oxford Exchange Blvd, Oxford, AL 36203-3459",
#   "Address.IntersectionDescription": "SEC I-20 & Golden Creek Rd",
#   "Address.Latitude": "33.608825",
#   "Address.Longitude": "-85.783182",
#   "Address.PostalCode": "36203-3459",
#   "Address.Subdivision": "AL",
#   "AlternateIdentifier.ID": "T2153",
#   "ID": "2153",
#   "IsDaylightSavingsTimeRecognized": "TRUE",
#   "LocationMilestones.LastRemodelDate": "",
#   "LocationMilestones.OpenDate": "2006-07-19T12:00:00",
#   "Market": "ESE",
#   "Name": "Oxford",
#   "OperatingHours..timeFormat": "12-hour",
#   "Store.StoreDistrictID": "340",
#   "Store.StoreGroupID": "394",
#   "Store.StoreRegionID": "300",
#   "SubTypeDescription": "",
#   "TimeZone.TimeZoneCode": "CST",
#   "TimeZone.TimeZoneDescription": "Central Std Time",
#   "TimeZone.TimeZoneOffset.OffsetCode": "UTC",
#   "TimeZone.TimeZoneOffset.OffsetHours": "-6",
#   "TypeCode": "STR",
#   "PhoneNumber": "(256) 231-2900",
#   "FaxNumber": "(256) 231-2910",
#   "BeginTime.MF": "8:00:00",
#   "Is24Hours.MF": false,
#   "IsOpen.MF": true,
#   "Summary.MF": "8:00 a.m.-10:00 p.m.",
#   "ThruTime.MF": "22:00:00",
#   "BeginTime.Sat": "8:00:00",
#   "Is24Hours.Sat": false,
#   "IsOpen.Sat": true,
#   "Summary.Sat": "8:00 a.m.-11:00 p.m.",
#   "ThruTime.Sat": "23:00:00",
#   "BeginTime.Sun": "8:00:00",
#   "Is24Hours.Sun": false,
#   "IsOpen.Sun": true,
#   "Summary.Sun": "8:00 a.m.-10:00 p.m.",
#   "ThruTime.Sun": "22:00:00",
#   "AllCapability": [
#     "CVS pharmacy",
#     "Caf\u00e9",
#     "Mobile Kiosk",
#     "Starbucks",
#     "Wine & Beer Available"
#   ]
# }

# 1) Create Bar Graph Showing Number of Stores by State/Subdivision

# 2) Create Line Graph Showing the Number of Stores Opened Each Year

# 3) Create a Line Graph Showing the change in total number of Target Stores over time
