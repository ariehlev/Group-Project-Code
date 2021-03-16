"""
The following code extracts features for all files in a given directory and outputs a csv file for each given file
to another directory. The features extracted in this case are: Root Mean Square (RMS), Mean Absolute Value (MAV),
Standard Deviation (SD), and Entropy
"""


import pandas as pd
import numpy as np
from scipy.stats import entropy
import os

path_to_raw_files = ""  # Should include the path to the files from where we want to extract features from

directory = os.listdir(path_to_raw_files)
os.chdir(path_to_raw_files)

output_path = ""  # Should include the path where we want to output our csv files

for file in directory:  # Loop that goes for every file in the given directory
    df = pd.read_csv(file)  # Reading csv file into a pandas dataframe

    """
    In our case, all filtered files after signal processing have the same ending "filtered.csv". To create a new 
    name for each file in the directory I am replacing the "filtered.csv" ending for a "features.csv" ending in the 
    line of code below
    """
    new_name = file[:-12] + "features.csv"

    """
    The next two lines are not necessary for the code to work properly. However, it helps to check on the progress
    of the feature extraction process
    """
    print(file)  # Printing name of the file being processed
    print(new_name)  # Printing the new name (output file name)

    end_path = (
        output_path + new_name
    )  # creating path for the output including the name of the end file

    del df["Unnamed: 0"]  # Deleting unnecessary column from the dataframe

    # Renaming columns to a programming friendly format. This part will change depending on the format of your input file
    df = df.rename(
        columns={
            "AI3_binary": "binary",
            "AI0 (V)": "a0",
            "AI1 (V)": "a1",
            "AI2 (V)": "a2",
            "AI3 (V)": "a3",
            "channel_binary": "movement",
        }
    )

    # creating empty arrays that will contain all the features
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

    entropy_0_col = []
    entropy_1_col = []
    entropy_2_col = []
    entropy_3_col = []

    movement_col = []

    """
    Our input csv file has a binary column that was renamed "movement" which takes a value of 1 when there was
    Maximal Voluntary Contraction (MVC) and a value of 0 for resting period. The way the recording was performed
    was by contracting and relaxing in periods of 3 seconds. Therefore, for the "movement" column, we get a group 
    of 0s (rest), then a group of 1s (MVC), then another group of 0s (rest), ... and so on until the end of the 
    recording. What we want to do is to extract features for each MVC and each rest period, meaning extracting 
    features for each group of 0s and each group of 1s. The following algorithm goes over the whole movement column 
    and saves the indexes when there is a change in this column (from both 0 to 1 or from 1 to 0). Thus, making it 
    possible to extract features for each MVC and resting period.
    """

    start_index = 0
    start_movement = df.iloc[0]["movement"]

    for i, row in df.iterrows():
        if i + 1 >= len(df["movement"]):  # We finished reading the data
            rms_0 = np.sqrt((df[int(start_index) :]["a0"] ** 2).mean())
            rms_1 = np.sqrt((df[int(start_index) :]["a1"] ** 2).mean())
            rms_2 = np.sqrt((df[int(start_index) :]["a2"] ** 2).mean())
            rms_3 = np.sqrt((df[int(start_index) :]["a3"] ** 2).mean())

            mean_0 = df[int(start_index) :]["a0"].mean()
            mean_1 = df[int(start_index) :]["a1"].mean()
            mean_2 = df[int(start_index) :]["a2"].mean()
            mean_3 = df[int(start_index) :]["a3"].mean()

            sd_0 = df[int(start_index) :]["a0"].std()
            sd_1 = df[int(start_index) :]["a1"].std()
            sd_2 = df[int(start_index) :]["a2"].std()
            sd_3 = df[int(start_index) :]["a3"].std()

            ent_0 = entropy(df[int(start_index) :]["a0"])
            ent_1 = entropy(df[int(start_index) :]["a1"])
            ent_2 = entropy(df[int(start_index) :]["a2"])
            ent_3 = entropy(df[int(start_index) :]["a3"])

            movement = df.iloc[i - 1]["movement"]

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

            entropy_0_col.append(ent_0)
            entropy_1_col.append(ent_1)
            entropy_2_col.append(ent_2)
            entropy_3_col.append(ent_3)

            movement_col.append(movement)

        if df.iloc[i]["movement"] != start_movement:  # We are still reading data
            rms_0 = np.sqrt((df[int(start_index) : i]["a0"] ** 2).mean())
            rms_1 = np.sqrt((df[int(start_index) : i]["a1"] ** 2).mean())
            rms_2 = np.sqrt((df[int(start_index) : i]["a2"] ** 2).mean())
            rms_3 = np.sqrt((df[int(start_index) : i]["a3"] ** 2).mean())

            mean_0 = df[int(start_index) : i]["a0"].mean()
            mean_1 = df[int(start_index) : i]["a1"].mean()
            mean_2 = df[int(start_index) : i]["a2"].mean()
            mean_3 = df[int(start_index) : i]["a3"].mean()

            sd_0 = df[int(start_index) : i]["a0"].std()
            sd_1 = df[int(start_index) : i]["a1"].std()
            sd_2 = df[int(start_index) : i]["a2"].std()
            sd_3 = df[int(start_index) : i]["a3"].std()

            ent_0 = entropy(df[int(start_index) : i]["a0"])
            ent_1 = entropy(df[int(start_index) : i]["a1"])
            ent_2 = entropy(df[int(start_index) : i]["a2"])
            ent_3 = entropy(df[int(start_index) : i]["a3"])

            movement = df.iloc[i - 1]["movement"]

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

            entropy_0_col.append(ent_0)
            entropy_1_col.append(ent_1)
            entropy_2_col.append(ent_2)
            entropy_3_col.append(ent_3)

            movement_col.append(movement)

            start_index = i
            start_movement = df.iloc[start_index]["movement"]

    data_final = {
        "rms_0": rms_0_col,
        "rms_1": rms_1_col,
        "rms_2": rms_2_col,
        "rms_3": rms_3_col,
        "mean_0": mean_0_col,
        "mean_1": mean_1_col,
        "mean_2": mean_2_col,
        "mean_3": mean_3_col,
        "sd_0": sd_0_col,
        "sd_1": sd_1_col,
        "sd_2": sd_2_col,
        "sd_3": sd_3_col,
        "entropy_0": entropy_0_col,
        "entropy_1": entropy_1_col,
        "entropy_2": entropy_2_col,
        "entropy_3": entropy_3_col,
        "movement": movement_col,
    }
    df_final = pd.DataFrame(
        data_final,
        columns=[
            "rms_0",
            "rms_1",
            "rms_2",
            "rms_3",
            "mean_0",
            "mean_1",
            "mean_2",
            "mean_3",
            "sd_0",
            "sd_1",
            "sd_2",
            "sd_3",
            "entropy_0",
            "entropy_1",
            "entropy_2",
            "entropy_3",
            "movement",
        ],
    )
    df_final.to_csv(end_path)  # converting pandas dataframe to csv
