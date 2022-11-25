#!\bin\env python

import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="71">
            <id>009</id>
            <name>Patrick</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring((input))
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print("Name", item.find('name').text)
    print("ID", item.find('id').text)
    print("Attribute", item.get("x"))
    
