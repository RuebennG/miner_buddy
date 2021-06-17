from pyadl import *
import pandas as pd
import psutil


class AMDGPUS:
    devices = ADLManager.getInstance().getDevices()
    number_of_GPUS = len(devices)

    def temperature(self):
        temps_data = []
        for device in self.devices: 
            d0 = device.adapterName.decode("utf-8")
            d1 = 80 #getCurrentTemperature()
            temps_data.append([d0, d1])
        return pd.DataFrame(temps_data)

    def usage(self):
        temps_data = []
        for device in self.devices:
            d0 = device.adapterName.decode("utf-8")
            d1 = device.getCurrentUsage()
            temps_data.append([d0, d1])

        return pd.DataFrame(temps_data)

# class AMDCPUS:
    
for process in psutil.process_iter():
    try:
    # get the number of CPU cores that can execute this process
        cores = len(process.cpu_affinity())
        print(cores)
    except psutil.AccessDenied:
        cores = 0

psutil.sensors_temperatures()

