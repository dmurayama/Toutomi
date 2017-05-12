import sys
sys.path.append('../python-fitbit/')
import fitbit
import gather_keys_oauth2 as Oauth2
import matplotlib.pyplot as plt
import numpy as np
 
"""for OAuth2.0"""
USER_ID = "228J35"
CLIENT_SECRET = "d0505bed8ffa8ba6a10bc4c895473047"
 
"""for obtaining Access-token and Refresh-token"""
server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()
 
token = server.fitbit.client.session.token
ACCESS_TOKEN = token["access_token"]
REFRESH_TOKEN = token["refresh_token"]
print("Access-token = {}".format(ACCESS_TOKEN))
print("Refresh-token = {}".format(REFRESH_TOKEN))
 
"""Authorization"""
auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
 
"""Getting data"""
fitbit_stats = auth2_client.intraday_time_series('activities/heart', base_date="2017-05-12", detail_level='1sec')
 
"""Getting only 'heartrate' and 'time'"""
stats = fitbit_stats['activities-heart-intraday']['dataset']
#print(stats)
 
"""Timeseries data of Heartrate"""
f1 = open('dataHR-timeseries.txt', 'w')
HR = []
for var in range(0, len(stats)):
    f1.write(stats[var]['time'])
    f1.write("\t")
    f1.write(str(stats[var]['value']))
    f1.write("\n")
    HR = HR + [stats[var]['value']]

f1.close()
plt.plot(HR)
plt.show()
