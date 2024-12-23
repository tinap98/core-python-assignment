def search_patients_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]

patients = []
num_patients = int(input("Enter the number of patients: "))

for _ in range(num_patients):
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    disease = input("Enter patient's disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})

search_disease = input("\nEnter disease to search for patients: ")
result = search_patients_by_disease(patients, search_disease)

if result:
    print(f"Patients with {search_disease}: {result}")
else:
    print(f"No patients found with {search_disease}.")
