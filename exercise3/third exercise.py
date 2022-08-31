gender = input("Please insert your gender: ")
hemoglobin_value = int(input("Please insert your hemoglobin value: "))
if gender.lower() == "male":
    if 117<=hemoglobin_value<=155:
        print("normal")
    elif hemoglobin_value<117:
        print("low")
    elif hemoglobin_value>155:
        print("high")

elif gender.lower() == "female":
    if 134<=hemoglobin_value<=167:
        print("normal")
    elif hemoglobin_value<134:
        print("low")
    elif hemoglobin_value>167:
        print("high")
else:
    print("Invalid input")