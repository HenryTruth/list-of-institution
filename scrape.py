from bs4 import BeautifulSoup
import requests
import json


# Url to get the list of instution
source = requests.get('https://www.4icu.org/ng/a-z/').text
soup = BeautifulSoup(source, 'lxml')


#Loop through the table tag of institution name and add it to the a list
institution_list = []
for i in soup.find_all('td'):
    try:
        if i.a.text != None:
            institution_list.append(i.a.text)
    except:
        pass
# print(institution_list)
# print(institution_list)
# Loop through the instituion list conver it to a dictionary then add it to ththe list
# result = []
# for i in institution_list:
#     print(i)

# # print(result)

# print(json.dumps(institution_list))
# convert the list of dictionary to json and write it to the approprait file
with open('list_of_univeristy.json','w') as f:
    json.dump(institution_list, f)