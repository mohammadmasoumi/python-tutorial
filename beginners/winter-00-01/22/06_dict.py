d = {
    "a": {
        "b": [1, 2, 3,   {"c": {"d": [{"e": 12, "g": 13}   ]}}]
    }
}

print(d.get("a"), type(d.get("a")))
print(           d.get("a").get("b")        , type(d.get("a").get("b")))
print(           d.get("a").get("b")[3]        , type(d.get("a").get("b")[3]))
print(           d.get("a").get("b")[3].get("c")        , type(d.get("a").get("b")[3].get("c") ))
print(           d.get("a").get("b")[3].get("c").get("d")        , type(d.get("a").get("b")[3].get("c").get("d") ))
print(           d.get("a").get("b")[3].get("c").get("d")[0]        , type(d.get("a").get("b")[3].get("c").get("d")[0] ))
print(           d.get("a").get("b")[3].get("c").get("d")[0].get("g")        , type(d.get("a").get("b")[3].get("c").get("d")[0].get("g") ))
