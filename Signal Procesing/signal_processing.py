import pywt
import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import denoise_wavelet
import pandas as pd

#funcion for plotting the graph with a selection of data - can be adjusted to show filtered, non-filtered and spliced data
def plot_stuff(raw1,raw2,raw3,raw4,denoised1,denoised2,denoised3,denoised4,denoised_bin):
    fig = plt.figure()
    plt.suptitle('Subject 5; Control; Flexion',weight="bold")
    plt.subplot(2,2,1)
    plt.plot(denoised1,'g')
    plt.ylim([0,6])
    plt.xlabel('Samples',weight="bold")
    plt.ylabel('Voltage Amplitude (V)',weight="bold")
    plt.title('Channel 1',weight="bold")
    plt.subplot(2,2,2) 
    plt.plot(denoised2)
    plt.ylim([0,6])
    plt.xlabel('Samples',weight="bold")
    plt.ylabel('Voltage Amplitude (V)',weight="bold")
    plt.title('Channel 2',weight="bold")
    plt.subplot(2,2,3)
    plt.plot(denoised3,'r')
    plt.ylim([0,6])
    plt.xlabel('Samples',weight="bold")
    plt.ylabel('Voltage Amplitude (V)',weight="bold")
    plt.title('Channel 3',weight="bold")
    plt.subplot(2,2,4) 
    plt.plot(denoised4,'y')
    plt.ylim([0,6])
    plt.xlabel('Samples',weight="bold")
    plt.ylabel('Voltage Amplitude (V)',weight="bold")
    plt.title('Channel 4',weight="bold")
    plt.tight_layout()
    plt.show()

#function for creating the file with processed data 
def output_stuff(list1,list2,list3,list4,list5,list6):
    df_out=pd.DataFrame({'Time (s)':list1,'AI0 (V)':list2,'AI1 (V)':list3,'AI2 (V)':list4,'AI3 (V)':list5,'channel_binary':list6})
    df_out.to_csv(r'D:\Coding\Year 3\group_project\done\ce\Nic, Flexion, Dry CE, 1 filtered.csv')


#code for opening the file with data and importing the 4 channels and time stamps into python code
collumns=["Time (s)","AI0 (V)","AI1 (V)","AI2 (V)","AI3 (V)"]
df = pd.read_csv (r'D:\Coding\Year 3\group_project\unfiltered\Ivan\Ivan S, Flexion, Regular Electrodes, 3.csv', usecols=lambda x: x in collumns,header=6)

#organises the imported data into lists
time_list=df['Time (s)'].to_list()
mylist1 = df['AI0 (V)'].to_list()
mylist2 = df['AI1 (V)'].to_list()
mylist3 = df['AI2 (V)'].to_list()
mylist4 = df['AI3 (V)'].to_list()
data1 = np.array(mylist1, dtype=np.float32)
data2 = np.array(mylist2, dtype=np.float32)
data3 = np.array(mylist3, dtype=np.float32)
data4 = np.array(mylist4, dtype=np.float32)


#extra code used for possible voltage offset correction
#for i in range(len(data1)):
   # data1[i]-=1.5
   # data2[i]-=1.5
   # data3[i]-=1.5
   # data4[i]-=1.3

#code for applying wavelet transform to the data; the parameters of the transform (function type, wavelet level, etc) can be changed here
x_denoise1=denoise_wavelet(data1,method='VisuShrink',mode='soft',wavelet_levels=4,wavelet='haar',rescale_sigma='True')
x_denoise2=denoise_wavelet(data2,method='VisuShrink',mode='soft',wavelet_levels=4,wavelet='haar',rescale_sigma='True')
x_denoise3=denoise_wavelet(data3,method='VisuShrink',mode='soft',wavelet_levels=4,wavelet='haar',rescale_sigma='True')
x_denoise4=denoise_wavelet(data4,method='VisuShrink',mode='soft',wavelet_levels=4,wavelet='haar',rescale_sigma='True')

#makes all values of the processed signal absolute
x_denoise1=abs(x_denoise1)    
x_denoise2=abs(x_denoise2)  
x_denoise3=abs(x_denoise3)  
x_denoise4=abs(x_denoise4)  

#creates a list for splicing data - the peaks will be marked as 1s in this list and the rest as 0s    
x_denoise_binary=[0]*len(x_denoise1)

#for loop for which goes through the channel lists and marks the peaks in binary list; by knowing time stamps and looking at plotted data, the ranges can be adjusted to produce the best results
for i in range(30000,len(x_denoise1),30000):
    for j in range(i,i+16000,1):
        x_denoise1_binary[j]=1

#two functions calls - one for plotting the data and the other for producing the file with the processed data    
plot_stuff(data1,data2,data3,data4,x_denoise1,x_denoise2,x_denoise3,x_denoise4,x_denoise_binary)
#output_stuff(time_list,x_denoise1,x_denoise2,x_denoise3,x_denoise4,x_denoise_binary)

print("done!")
