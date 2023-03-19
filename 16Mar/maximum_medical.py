def max_viset_speciality(patienr_medical_speciality_list,medical_speciality):
    max_viste=0
    P=patienr_medical_speciality_list.count('P')
    E=patienr_medical_speciality_list.count('E')
    O=patienr_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality
#patienr_medical_speciality_list=[301,'P',302,'E',305,'O']
patienr_medical_speciality_list = input("Enter values separated by commas: ") 
my_list = patienr_medical_speciality_list.split(",")
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"Ent"}
speciality=max_viset_speciality(patienr_medical_speciality_list,medical_speciality)
print(speciality)