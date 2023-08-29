import re
import csv
def fix_phone_number(phone_number):
    pattern = r"(\+7|8)?\s*\(*(\d{3})\)*\s*(-+\s*)?(\d{3})\s*(-+\s*)?(\d{2})\s*(-+\s*)?(\d{2})\s*(доб\.\s*(\d+))?"
    match = re.match(pattern, phone_number)
    if match:
        number = match.group(2) + match.group(4) + match.group(6) + match.group(8)
        if match.group(10):
            number += " доб." + match.group(10)
        return "+7(" + number + ")"
    else:
        return phone_number
def fix_contacts(contacts_list):
    fixed_contacts = []
    for contact in contacts_list:
        lastname = contact[0]
        firstname = contact[1]
        surname = contact[2]
        organization = contact[3]
        position = contact[4]
        phone = fix_phone_number(contact[5])
        email = contact[6]

        fixed_contacts.append([lastname, firstname, surname, organization, position, phone, email])

    return fixed_contacts

def merge_duplicate_contacts(contacts_list):
    merged_contacts = []
    unique_contacts = {}

    for contact in contacts_list:
        key = (contact[0], contact[1], contact[2])

        if key not in unique_contacts:
            unique_contacts[key] = contact
        else:
            merged_contacts.remove(unique_contacts[key])
            merged_contacts.append(contact)

    merged_contacts = list(unique_contacts.values()) + merged_contacts
    return merged_contacts


# Чтение адресной книги из файла
with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    contacts_list = list(reader)

# Фиксирование телефонов и контактов
contacts_list = fix_contacts(contacts_list)
contacts_list = merge_duplicate_contacts(contacts_list)

# Запись адресной книги в новый файл
with open("phonebook.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(contacts_list)
