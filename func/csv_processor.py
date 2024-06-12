import pandas as pd


def load_csv():
    df = pd.read_csv("field_of_study_exercise.csv")
    df = df[['field_of_study', 'academic_field']]
    total_len = df.shape[0]
    df_clean = df.dropna()
    missing_count = total_len - df_clean.shape[0]
    mapping_ratio = missing_count / total_len
    print("missing_count : " ,  missing_count)
    print("mapping_ratio : ", mapping_ratio)
    print(df_clean)
    return df_clean

def add_csv(field_of_study, academic_field):
    string = ",," + field_of_study + "," + academic_field
    with open("field_of_study_exercise.csv", "a") as myfile:
        myfile.write(string)
        myfile.write("\n")