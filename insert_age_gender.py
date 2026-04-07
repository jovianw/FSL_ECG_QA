import json
import sys
import os
import os.path
import pandas as pd

"""
Add age and gender questions to each entry's question field.
"""
def add_age_gender_questions(data: list[dict], ecg_df: pd.DataFrame) -> list[dict]:
    
    for entry in data:
        # print(entry)
        # print(ecg_df[ecg_df['ecg_id'] == entry["ecg_id"][0]])

        row = ecg_df[ecg_df['ecg_id'] == entry["ecg_id"][0]].iloc[0]

        # age, gender = None, None
        age = str(row.get("age", "unknown"))
        gender = "Male" if row.get("sex", "unknown") == 0 else "Female"
    
        age_gender_question = f" Given that patient is {gender} and is {age} years old."
        entry["question"] = entry["question"] + age_gender_question
    
    return data

def main():
    # print('start')
    ecg_df = pd.read_csv('./ptbxl_database.csv')
    # print(f'df: {ecg_df.shape}')


    # for dirpath, dirnames, filenames in os.walk("./ecgqa/ptbxl"):
    for dirpath, dirnames, filenames in os.walk("./ecgqa/ptbxl/paraphrased/train"):
        # for filename in [f for f in filenames if f.endswith(".json")]:
        for filename in [f for f in filenames if f.endswith("000000.json")]:
            # print(os.path.join(dirpath, filename))
            with open(os.path.join(dirpath, filename), "r") as jsonfile:
                data = json.load(jsonfile)
                if isinstance(data, dict):
                    data = [data]
                updated_data = add_age_gender_questions(data, ecg_df)

            with open(os.path.join(dirpath, filename), "w") as jsonfile:
                json.dump(updated_data, jsonfile, indent=4)

            print(f"Updated {filename}.")


if __name__ == "__main__":
    main()
