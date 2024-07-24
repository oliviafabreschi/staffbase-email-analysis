# Olivia Fabreschi 17 Nov 2023
# created to analyse emails from staffbase/bananatag
# Using imported json from the staffbase analytics page


import json

filepath = "emaildatainjson.json"

with open(filepath, 'r') as file:
    data = json.load(file)

# print(data['subject'])
# print(data['timeSent'])
# print(data['uniOpens'])
# print(data['uniClicks'])

# print(data[1]) each individual email item in list

# 37 is total length of data

data2022Subjects = []
data2023Subjects = []

data2022views= []
data2023views= []

data2022clicks= []
data2023clicks = []

for i in range(len(data)):
    if ("2023" in (data[i]["timeSent"])):
        data2023Subjects.append(data[i]["subject"])
        data2023views.append(data[i]["uniOpens"])
        data2023clicks.append(data[i]["uniClicks"])


    else:
        data2022Subjects.append(data[i]["subject"])
        data2022views.append(data[i]["uniOpens"])
        data2022clicks.append(data[i]["uniClicks"])

# finding averages for 2023
averageViews2023 = 0;
for d in data2023views:
    averageViews2023 += d;
averageViews2023 = averageViews2023/len(data2023views);

averageClicks2023 = 0;
for d in data2023clicks:
    averageClicks2023 += d;
averageClicks2023 = averageClicks2023/len(data2023clicks);


# finding data for 2022
averageViews2022 = 0;
for d in data2022views:
    averageViews2022 += d;
averageViews2022  = averageViews2022/len(data2022views);

averageClicks2022 = 0;
for d in data2022clicks:
    averageClicks2022 += d;
averageClicks2022 = averageClicks2022/len(data2022clicks);


# printing results

print(f"average views 2023 are: {averageViews2023}")
print(f"average views 2022 are: {averageViews2022}")
print(" ")

print(f"average clicks 2023 are: {averageClicks2023}")
print(f"average clicks 2022 are: {averageClicks2022}")



# finding the names of the top posts
maxviews2022 = max(data2022views)
print(f"max views 2022 are: {maxviews2022}")

maxClicks2022 = max(data2022clicks)
print(f"max clicks 2022 are: {maxClicks2022}")

for i in range(len(data2022views)):
    if data2022views[i] == maxviews2022:
        print(f"Name of email with max views 2022 is: {data2022Subjects[i]}")

for i in range(len(data2022clicks)):
    if data2022clicks[i] == maxClicks2022:
        print(f"Name of email with max clicks 2022 is: {data2022Subjects[i]}")

print("")
maxClicks2023 = max(data2023clicks)
print(f"max clicks 2023 are: {maxClicks2023}")

maxviews2023 = max(data2023views)
print(f"max views 2023 are: {maxviews2023}")

for i in range(len(data2023views)):
    if data2023views[i] == maxviews2023:
        print(f"Name of email with max views 2023 is: {data2023Subjects[i]}")

for i in range(len(data2023clicks)):
    if data2023clicks[i] == maxClicks2023:
        print(f"Name of email with max clicks 2022 is: {data2023Subjects[i]}")

# total numbers

# finding averages for 2023
totalViews2023 = 0;
for d in data2023views:
    totalViews2023 += d;


totalClicks2023 = 0;
for d in data2023clicks:
    totalClicks2023 += d;


# finding data for 2022
totalViews2022 = 0;
for d in data2022views:
    totalViews2022 += d;


totalClicks2022 = 0;
for d in data2022clicks:
    totalClicks2022 += d;



print("")
print(f"total clicks 2023 are: {totalClicks2023}")
print(f"total clicks 2022 are: {totalClicks2022}")
print(f"total views 2023 are: {totalViews2023}")
print(f"total views 2022 are: {totalViews2022}")

