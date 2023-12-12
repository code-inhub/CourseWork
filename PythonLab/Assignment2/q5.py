def find_max_visited_speciality(visits):
    specialities = {
        "P": "Pediatrics",
        "O": "Orthopedics",
        "E": "ENT"
    }

    visit_counts = {}
    for i in range(0, len(visits), 2):
        patient_speciality = visits[i + 1]
        visit_counts[patient_speciality] = visit_counts.get(patient_speciality, 0) + 1

    max_speciality = max(visit_counts, key=visit_counts.get)
    return specialities[max_speciality]


input1 = [101, 'P', 102, 'O', 302, 'P', 305, 'P']
input2 = [101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'O']
input3 = [101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O', 987, 'E']


print(find_max_visited_speciality(input1))  
print(find_max_visited_speciality(input2)) 
print(find_max_visited_speciality(input3))