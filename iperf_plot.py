import plotly.express as px
import pandas as pd

def main():
    distances = [3, 5, 7, 8, 10]
    for distance in distances:
        data = []
        tcp_data = pd.read_csv("iperf_tcp_" + str(distance) +"m.csv")
        udp_data = pd.read_csv("iperf_udp_" + str(distance) +"m.csv")

        tcp_row = tcp_data[" Run1"].values[0] #all 5 values stored in Run1 
        tcp_row = tcp_row.split() #parse into a Python float list
        for i in range (len(tcp_row)):
            tcp_row[i]=float(tcp_row[i])

        udp_row = udp_data[" Run1"].values[0] #all 5 values stored in Run1 
        udp_row = udp_row.split() #parse into a Python float list
        for i in range (len(udp_row)):
            udp_row[i]=float(udp_row[i])
        for i in range(5):
            data.append(("Run "+ str(i+1), tcp_row[i], udp_row[i]))
        df = pd.DataFrame(data, columns = ['Test Runs', 'TCP Throughput (Mbps)', 'UDP Throughput (Mbps)'])  #put data into dataframe

        fig = px.line(df, x="Test Runs", y=df.columns[1:], title="TCP & UDP Throughput at " + str(distance) + "m Distance", markers=True, labels={"value": "Throughput (Mbps)"})
        fig.write_image("throughputs_graph_" + str(distance) + "m.png")

        


if __name__ == "__main__":
    main()
