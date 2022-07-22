# replace key

d = {
    "shahr": "varamin",
    "name": "asghar"
}

# "shahr" -> "city"
# upsert=> update/insert
# d["shahr"] = "city"
d["city"] = d.pop("shahr")

print(d)