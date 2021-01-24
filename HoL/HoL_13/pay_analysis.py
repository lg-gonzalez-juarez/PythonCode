from csv import DictReader

employee_info = []
with open("employees.csv", newline="") as f:
    reader = DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        row["salary"] = float(row["salary"])
        employee_info.append(row)

# Example dictionary in employee_info
# {
#     "id": "10",
#     "first_name": "Marie-ann",
#     "last_name": "Cargo",
#     "email": "Marie-ann.Cargo@example.com",
#     "gender": "Female",
#     "age": 68,
#     "salary": 54000.0,
#     "job_title": "Human Resources Manager",
# }
