import pandas as pd
import numpy as np
import scipy
from numpy import mean, absolute
from scipy.stats import entropy
import os, re

directory = os.listdir('/Users/arieh/Desktop/Imperial/3rd_year/Group Project/recordings/ce_nic')
os.chdir('/Users/arieh/Desktop/Imperial/3rd_year/Group Project/recordings/ce_nic')

for file in directory:
    df = pd.read_csv(file)
    new_name = file[:-12] + "features.csv"
    print(file)
    print(new_name)

    del df['Unnamed: 0']

    df = df.rename(columns={"AI3_binary": "binary", "AI0 (V)": "a0", "AI1 (V)": "a1", "AI2 (V)": "a2",
                            "AI3 (V)": "a3", "channel_binary": "movement"})

    rms_0_col = []
    rms_1_col = []
    rms_2_col = []
    rms_3_col = []

    mean_0_col = []
    mean_1_col = []
    mean_2_col = []
    mean_3_col = []

    sd_0_col = []
    sd_1_col = []
    sd_2_col = []
    sd_3_col = []

    var_0_col = []
    var_1_col = []
    var_2_col = []
    var_3_col = []

    entropy_0_col = []
    entropy_1_col = []
    entropy_2_col = []
    entropy_3_col = []

    movement_col = []

    start_index = 0
    start_movement = df.iloc[0]['movement']

    for i, row in df.iterrows():
        if i + 1 >= len(df['movement']):  # We finished reading the data
            rms_0 = np.sqrt((df[int(start_index):]['a0'] ** 2).mean())
            rms_1 = np.sqrt((df[int(start_index):]['a1'] ** 2).mean())
            rms_2 = np.sqrt((df[int(start_index):]['a2'] ** 2).mean())
            rms_3 = np.sqrt((df[int(start_index):]['a3'] ** 2).mean())

            mean_0 = df[int(start_index):]['a0'].mean()
            mean_1 = df[int(start_index):]['a1'].mean()
            mean_2 = df[int(start_index):]['a2'].mean()
            mean_3 = df[int(start_index):]['a3'].mean()

            sd_0 = df[int(start_index):]['a0'].std()
            sd_1 = df[int(start_index):]['a1'].std()
            sd_2 = df[int(start_index):]['a2'].std()
            sd_3 = df[int(start_index):]['a3'].std()

            var_0 = df[int(start_index):]['a0'].var()
            var_1 = df[int(start_index):]['a1'].var()
            var_2 = df[int(start_index):]['a2'].var()
            var_3 = df[int(start_index):]['a3'].var()

            ent_0 = entropy(df[int(start_index):]['a0'])
            ent_1 = entropy(df[int(start_index):]['a1'])
            ent_2 = entropy(df[int(start_index):]['a2'])
            ent_3 = entropy(df[int(start_index):]['a3'])

            movement = df.iloc[i - 1]['movement']

            rms_0_col.append(rms_0)
            rms_1_col.append(rms_1)
            rms_2_col.append(rms_2)
            rms_3_col.append(rms_3)

            mean_0_col.append(mean_0)
            mean_1_col.append(mean_1)
            mean_2_col.append(mean_2)
            mean_3_col.append(mean_3)

            sd_0_col.append(sd_0)
            sd_1_col.append(sd_1)
            sd_2_col.append(sd_2)
            sd_3_col.append(sd_3)

            var_0_col.append(var_0)
            var_1_col.append(var_1)
            var_2_col.append(var_2)
            var_3_col.append(var_3)

            entropy_0_col.append(ent_0)
            entropy_1_col.append(ent_1)
            entropy_2_col.append(ent_2)
            entropy_3_col.append(ent_3)

            movement_col.append(movement)

        if df.iloc[i]['movement'] != start_movement:
            rms_0 = np.sqrt((df[int(start_index):i]['a0'] ** 2).mean())
            rms_1 = np.sqrt((df[int(start_index):i]['a1'] ** 2).mean())
            rms_2 = np.sqrt((df[int(start_index):i]['a2'] ** 2).mean())
            rms_3 = np.sqrt((df[int(start_index):i]['a3'] ** 2).mean())

            mean_0 = df[int(start_index):i]['a0'].mean()
            mean_1 = df[int(start_index):i]['a1'].mean()
            mean_2 = df[int(start_index):i]['a2'].mean()
            mean_3 = df[int(start_index):i]['a3'].mean()

            sd_0 = df[int(start_index):i]['a0'].std()
            sd_1 = df[int(start_index):i]['a1'].std()
            sd_2 = df[int(start_index):i]['a2'].std()
            sd_3 = df[int(start_index):i]['a3'].std()

            var_0 = df[int(start_index):i]['a0'].var()
            var_1 = df[int(start_index):i]['a1'].var()
            var_2 = df[int(start_index):i]['a2'].var()
            var_3 = df[int(start_index):i]['a3'].var()

            ent_0 = entropy(df[int(start_index):i]['a0'])
            ent_1 = entropy(df[int(start_index):i]['a1'])
            ent_2 = entropy(df[int(start_index):i]['a2'])
            ent_3 = entropy(df[int(start_index):i]['a3'])

            movement = df.iloc[i - 1]['movement']

            rms_0_col.append(rms_0)
            rms_1_col.append(rms_1)
            rms_2_col.append(rms_2)
            rms_3_col.append(rms_3)

            mean_0_col.append(mean_0)
            mean_1_col.append(mean_1)
            mean_2_col.append(mean_2)
            mean_3_col.append(mean_3)

            sd_0_col.append(sd_0)
            sd_1_col.append(sd_1)
            sd_2_col.append(sd_2)
            sd_3_col.append(sd_3)

            var_0_col.append(var_0)
            var_1_col.append(var_1)
            var_2_col.append(var_2)
            var_3_col.append(var_3)

            entropy_0_col.append(ent_0)
            entropy_1_col.append(ent_1)
            entropy_2_col.append(ent_2)
            entropy_3_col.append(ent_3)

            movement_col.append(movement)

            start_index = i
            start_movement = df.iloc[start_index]['movement']

    data_final = {'rms_0': rms_0_col,
                  'rms_1': rms_1_col,
                  'rms_2': rms_2_col,
                  'rms_3': rms_3_col,
                  'mean_0': mean_0_col,
                  'mean_1': mean_1_col,
                  'mean_2': mean_2_col,
                  'mean_3': mean_3_col,
                  'sd_0': sd_0_col,
                  'sd_1': sd_1_col,
                  'sd_2': sd_2_col,
                  'sd_3': sd_3_col,
                  'var_0': var_0_col,
                  'var_1': var_1_col,
                  'var_2': var_2_col,
                  'var_3': var_3_col,
                  'entropy_0': entropy_0_col,
                  'entropy_1': entropy_1_col,
                  'entropy_2': entropy_2_col,
                  'entropy_3': entropy_3_col,
                  'movement': movement_col,
                  }
    df_final = pd.DataFrame(data_final, columns=['rms_0', 'rms_1', 'rms_2', 'rms_3',
                                                 'mean_0', 'mean_1', 'mean_2', 'mean_3',
                                                 'sd_0', 'sd_1', 'sd_2', 'sd_3',
                                                 'var_0', 'var_1', 'var_2', 'var_3',
                                                 'entropy_0', 'entropy_1', 'entropy_2', 'entropy_3',
                                                 'movement'])
    end_path = '/Users/arieh/Desktop/Imperial/3rd_year/Group Project/features/ce/' + new_name
    df_final.to_csv(end_path)