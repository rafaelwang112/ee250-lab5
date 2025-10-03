# Lab 5

## Team Members
Rafael Wang

## Lab Question Answers

Answer for Question 1: 
dBm is a measure of signal strength and is decibels relative to one milliwatt. Good values for
WiFi signal strength range from approximately -30 to -70 dBm. From -80 to -90 and beyond, the signal strength is considered bad.

Answer for Question 2:
The OS used needs to be first checked because different OS's use different commands to fetch the WiFi signal strength. The difference between the commands is that the Linux and Mac commands both return the signal strength directly in dBm while the Windows command returns the signal quality as a percentage, which is then converted into dBm by code.  

Answer for Question 3:
subprocess.check_output is like running commands in the terminal, except its done through Python using the given argument. It returns the output data of the command in bytes. 

Answer for Question 4:
re.search takes in a string and searches it to find the first occurence of the specified regex pattern. If the pattern is found, it returns a Match object. Otherwise, it returns None.

Answer for Question 5:
The signal quality needs to be converted to dBm because the Windows command returns signal quality as a percentage value ranging from 0 to 100, not directly in dBm. 

Answer for Question 6:
Standard deviation is a measure of how spread data is from the mean. It's useful to calculate it because it gives a sense of how much variation there is in the data.

Answer for Question 7:
A dataframe is a tabular data structure that stores data by columns and rows. Here, the columns represent the location, signal_strength_mean, and the signal_strength_std, while each row represents the data associated with each location. It's useful to store data this way because it not only visually represents the data well but it also makes plotting with Plotly simpler in the next step. 

Answer for Question 8:
It's important to plot error bars because it's important for engineers to have robust visuals to analyze and interpret. By including error bars, we can see key elements regarding the data that would not be obvious with just the mean. The error bars tell us how much the data varies from the mean value. 

Answer for Question 9:
From the plot, I observed there was a lot of variation regarding the mean signal strength value depending on what location I was at. As I went downstairs from my bedroom to my living room and kitchen, the signal strength got stronger. As I went back upstairs to my bathroom and then to the garage, the strength started becoming weaker again. I think the strength is weaker in certain locations because I am further away from my house's router and there are physical barriers in between my computer and the router. For example, since my router is located downstairs near the kitchen, the signal strength is a lot stronger than in my room or in the garage.

Answer for Question 10:
As distance increases, TCP and UDP throughput decrease. Near the router, there is high throughput but as the distance increases, it becomes lower because of decreased signal strength. This is particularly reflected in my TCP graphs.

Answer for Question 11:
Significant packet loss begins to occur at 15m+ for UDP. In my experiment, I wasn't able to test such long distances due to physical constraints but I did begin to notice losses on the receiver side when I did the experiment at 10m.

Answer for Question 12:
UDP has more packet loss than TCP because TCP will try to resend packets when they are lost, at the expense of deecreased speed. However, UDP does not resend, so its packet loss becomes a lot more pronounced at increased distances from the router.

Answer for Question 13:
If bandwidth is increased by changing it to -b 100M, the RPi will try to send at 100Mbps compared to the 10 that it currently sends at. 

Answer for Question 14:
Yes, on 5GHz Wi-Fi, throughput would be higher at closer ranges. However, it would decrease rapidly with distance. On the other hand, on 2.4GHz Wi-Fi, it may be a bit slower, but it handles distance better, so its throughput may not drastically decrease as quickly with distance. 
