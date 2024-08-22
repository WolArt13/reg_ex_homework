import re
from pprint import pprint
import csv

PHONE_PATTERN = r"(\+7|8)[\s(]*(\d{3})[)\s]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s(]*(доб.)*\s*(\d{4})*"
PHONE_SUB = r"+7(\2)\3-\4-\5 \6\7"

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def main(contacts:list):
    formatted_list = list()
    for item in contacts:
        full_name = " ".join(item[:3]).split(" ")
        row = [full_name[0], full_name[1], full_name[2], item[3], item[4], re.sub(PHONE_PATTERN, PHONE_SUB, item[5]), item[6]]
        formatted_list.append(row)

    return format(formatted_list)

def format(contact_list:list):
    for contact in contact_list:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in contact_list:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if last_name == new_last_name and first_name == new_first_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
    
    new_list = list()
    
    for i in contact_list:
        if i not in new_list:
            new_list.append(i)

    return new_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(main(contacts_list))