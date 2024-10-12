import pandas as pd
df=pd.read_csv('train_data_2024.csv')
print(df)
#count Train By Status
#Find Average Speed of all trains
avg_speed=df['Speed'].mean()
print(avg_speed)
#Identify Fastest Train: Which train has the highest speed, and what is its departure and arrival location?
high_Speed=df['Speed'].max()
train_details = df.loc[df['Speed'] == high_Speed, ['Deperture', 'Arrived']]
print("Deperture and arrived stations of Train having the max speed are",train_details)
#count the no of trains with higest speed
High_speed_count=df[df['Speed']==high_Speed]['Train No'].nunique() #.count will count duplicate train no //for unique train no use .nunique()
print("No of Higest speed Trains are : ",High_speed_count)
#Count Trains by Departure Location: How many trains depart from each location (e.g., Kolkata, Nagpur, etc.)?
l=set(df['Deperture'])
for i in l:
    Count_By_Deperture=df[df["Deperture"]==i]["Train No"].count()
    print(f"No of tranin from {i} is :",Count_By_Deperture)
#Trains with Duration Greater than a Threshold: How many trains have a duration of more than 12 hours?
Duration_more_Than_12=df[df["Duration"]>12]["Duration"].count()
print('No Trains having duration of 12 hours are: ', Duration_more_Than_12)
#Speed Distribution: What is the distribution of train speeds (e.g., count of trains in speed ranges: 50-70, 71-90, 91-110, 111-130, 131-150)?
bins = [50, 70, 90, 110, 130, 150]
labels = ['50-70', '71-90', '91-110', '111-130', '131-150']
df['Speed_Range'] = pd.cut(df['Speed'], bins=bins, labels=labels, include_lowest=True)
speed_distribution = df['Speed_Range'].value_counts().sort_index()
print(speed_distribution)
#Delayed Trains by Departure Location: How many delayed trains are there from each departure location?
Delayed_trains=df[df['Status']=='Delayed']['Train No'].count()
print("No of Delayed Trains are: ",Delayed_trains)
#Average Duration of Delayed Trains: What is the average duration of trains that are delayed?
Avg_Delay=df[df["Status"]=="Delayed"]["Duration"].mean()
print("Average Duration of Delayed Trains are: ",Avg_Delay)
#Find Unique Train Numbers: How many unique train numbers are there in the dataset?
unique_train=df['Train No'].nunique() #nunique will return the no of unique train no//.unique will return a list which contains the train no of unique values 
print("No of unique Train No are : ",unique_train)

#Trains Arrived in a Specific Location: How many trains arrived in "Kolkata"?
arrived_at_Kolkata=df[df['Arrived']=='Kolkata']['Train No'].count()
print("No of Trains arrived at kolkata are:",arrived_at_Kolkata)



