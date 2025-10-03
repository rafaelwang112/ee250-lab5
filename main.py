import platform
import time
import pandas as pd
import plotly.express as px
import numpy as np
import subprocess
import re

def get_wifi_signal_strength() -> int:
    """Get the signal strength of the wifi connection.
    
    Returns:
        The signal strength in dBm.
    """
    # Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
    #Answered in README
    # Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
    #Answered in README
    # Question 3: In your own words, what is subprocess.check_output doing? What does it return?
    # HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output
    #Answered in README
    # Question 4: In your own words, what is re.search doing? What does it return?
    # HINT: https://docs.python.org/3/library/re.html#re.search
    #Answered in README
    # Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
    # HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN
    #Answered in README
    if platform.system() == 'Linux': # Linux
        output = subprocess.check_output("iwconfig wlan0", shell=True)
        match = re.search(r"Signal level=(-?\d+) dBm", output.decode('utf-8'))
        signal_strength = int(match.group(1))
    elif platform.system() == 'Windows': # Windows
        output = subprocess.check_output("netsh wlan show interfaces", shell=True)
        match = re.search(r"Signal\s*:\s*(\d+)%", output.decode('utf-8'))
        signal_quality = int(match.group(1))
        signal_strength = -100 + signal_quality / 2
    elif platform.system() == 'Darwin': # Mac
        output = subprocess.check_output("wdutil info", shell=True, stderr=subprocess.STDOUT)
        # The new regex looks for "RSSI" (Received Signal Strength Indicator).
        match = re.search(r"RSSI\s+:\s*(-?\d+)", output.decode('utf-8', errors='ignore'))   
        signal_strength = int(match.group(1))
        print(signal_strength)
    else:
        raise Exception("Unknown OS")

    return signal_strength

def main():
    # Choose at least 5 locations to sample the signal strength at
    # These can be rooms in your house, hallways, different floors, outside, etc. (as long as you can get a WiFi signal)
    locations = ['bedroom', 'living room', 'kitchen', 'bathroom', 'garage']
    samples_per_location = 10 # number of samples to take per location
    time_between_samples = 1 # time between samples (in seconds)

    data = [] # list of data points
    for location in locations:
        print(f"Go to the {location} and press enter to start sampling")
        input() # wait for the user to press enter
        signal_strengths = [] # list of signal strengths at this location

        for i in range (0, samples_per_location): #for loop to get the 10 samples with 1 second in between
            signal_strengths.append(get_wifi_signal_strength())
            time.sleep(time_between_samples)
        
        signal_strength_mean = np.mean(signal_strengths) #calculating mean and standard deviation using np

        signal_strength_std = np.std(signal_strengths)

        # Question 6: What is the standard deviation? Why is it useful to calculate it?
        #Answered in README
        data.append((location, signal_strength_mean, signal_strength_std))

    # create a dataframe from the data
    df = pd.DataFrame(data, columns=['location', 'signal_strength_mean', 'signal_strength_std'])

    # Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
    # HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
    # HINT: print the dataframe to see what it looks like
    #Answered in README
    print(df)

    fig = px.bar(
        df, x = "location", y = "signal_strength_mean", error_y = "signal_strength_std" #plotting bar graph with error bars
    )
    # Question 8: Why is it important to plot the error bars? What do they tell us?
    #Answered in README

    # write the plot to a file - make sure to commit the PNG file to your repository along with your code
    fig.write_image("signal_strength.png")

    # Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?
    #             Why do you think signal strength is weaker in certain locations?
    #Answered in README


if __name__ == "__main__":
    main()
