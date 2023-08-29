import csv
import re
from pprint import pprint


def fix_contacts(contacts_list):
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'

    for contact in contacts_list[1:]:
        full_name = contact[0] + contact[1] + contact[2]
        name_parts = re.sub(name_pattern, name_substitution, full_name).split()

        if len(name_parts) == 3:
            contact[0] = name_parts[0]
            contact[1] = name_parts[1]
            contact[2] = name_parts[2]
        elif len(name_parts) == 2:
            contact[0] = name_parts[0]
            contact[1] = name_parts[1]
            contact[2] = ''
        elif len(name_parts) == 1:
            contact[0] = name_parts[0]
            contact[1] = ''
            contact[2] = ''

    return contacts_list


def fix_phone_numbers(contacts_list):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'

    for contact in contacts_list:
        contact[5] = phone_pattern.sub(phone_substitution, contact[5])

    return contacts_list


def duplicates():
    contact_list = {}
    for contacts in contacts_list[1:]:
        last_name = contacts[0]
        if last_name not in contact_list:
            contact_list[last_name] = contacts
        else:
            for id, item in enumerate(contact_list[last_name]):
                if item == '':
                    contact_list[last_name][id] = contacts[id]

    for last_name, contact in contact_list.items():
        for contacts in contact:
            if contact not in contacts_list_updated:
                contacts_list_updated.append(contact)
    return contacts_list_updated


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as in_file:
        rows = csv.reader(in_file, delimiter=",")
        contacts_list = list(rows)
        contacts_list_updated = []
        fix_contacts(contacts_list)
        fix_phone_numbers(contacts_list)
        duplicates()
    with open("phonebook.csv", "w", encoding="utf-8") as out_file:
        datawriter = csv.writer(out_file, delimiter=',')
        datawriter.writerows(contacts_list_updated)
    pprint(contacts_list_updated)
