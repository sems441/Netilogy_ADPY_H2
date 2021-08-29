from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import re
import csv


def search_duplex(data):
  for index, search in enumerate(results):
    if data[0] == search[0] and data[1] == search[1] and data not in results:
      digit = results.index(search)
      third_name = max(data[2], search[2])
      organization = max(data[3], search[3])
      position = max(data[4], search[4])
      phone = max(data[5], search[5])
      email = max(data[6], search[6])
      results[digit].clear()
      results[digit].append(data[0])
      results[digit].append(data[1])
      results[digit].append(third_name)
      results[digit].append(organization)
      results[digit].append(position)
      results[digit].append(phone)
      results[digit].append(email)
      return True
  return False

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
results = []

for index, line in enumerate(contacts_list):
  if index == 0:
    results.append(line)
    continue

  result = " ".join(line[:2])
  result = re.split("\W+", result)
  if len(result) == 4:
    result.pop()
  elif len(result) == 2:
    result.append("")
  result.append(line[3])
  result.append(line[4])
  result.append(re.sub(r"(\+7|8)\s?\(?(\(\w+\)|\w{3})\)?(\W?)(\w{3})(\W?)(\w{2})(\W?)(\w{2})(\s\(?\w+\.\s((\w{4}))\)?)?",
                       r"+7(\2)\4-\6-\8 доб.\11", line[5]))
  result.append(line[6])
  if search_duplex(result):
    continue
  results.append(result)

pprint(results)

# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(results)