from bs4 import BeautifulSoup
import requests
import json


# Url to get the list of instution
source = requests.get('https://en.wikipedia.org/wiki/List_of_colleges_of_education_in_Nigeria').text
soup = BeautifulSoup(source, 'lxml')


#Loop through the table tag of institution name and add it to the a list
institution_list = []
for i in soup.find_all('td'):
    try:
        if i.a.text != None:
            institution_list.append(i.a.text)
    except:
        pass


# Loop through the instituion list conver it to a dictionary then add it to ththe list
result = []
for i in institution_list:
    if 'College' in i:
        ds = {i:i}
        result.append(ds)

# print(result)

print(json.dumps(result, indent= 2))


# convert the list of dictionary to json and write it to the approprait file
with open('list_of_college.json','w') as f:
    json.dump(result, f)