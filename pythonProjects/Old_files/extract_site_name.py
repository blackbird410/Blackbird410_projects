def extract_site(url: str):
    li = ["http", "https", "www"]
    site_name = ""
    for x in url:
        if x.isalpha():
            site_name += x
        else:
            if site_name in li or site_name == "":
                site_name = ""
                continue
            else:
                return site_name


u = str(input("ENTER DOMAIN : "))
print(extract_site(u))
