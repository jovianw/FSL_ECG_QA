import json
import sys
import os
import os.path

def add_age_gender_questions(data: list[dict]) -> list[dict]:
    """
    Add age and gender questions to each entry's question field.
    """
    age_gender_question = " Given that patient is [GENDER] and is [AGE] years old."
    
    for entry in data:
        if "question" in entry:
            entry["question"] = entry["question"] + age_gender_question
    
    return data



def main():
    c = 0
    # for dirpath, dirnames, filenames in os.walk("./ecgqa/ptbxl/paraphrased/train"):
    for dirpath, dirnames, filenames in os.walk("./ecgqa/ptbxl"):
        for filename in [f for f in filenames if f.endswith(".json")]:
            # print(os.path.join(dirpath, filename))
            with open(os.path.join(dirpath, filename), "r") as jsonfile:
                data = json.load(jsonfile)
                if isinstance(data, dict):
                    data = [data]
                updated_data = add_age_gender_questions(data)

            with open(os.path.join(dirpath, filename), "w") as jsonfile:
                json.dump(updated_data, jsonfile, indent=4)

            print(f"Updated {filename}.")


if __name__ == "__main__":
    main()