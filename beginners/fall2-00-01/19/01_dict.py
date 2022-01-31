d = {
    "a": {
        "b": {
            "c": ["history", "art", {"d": {"e": "PE"}}]
        }
    }
}

print(d.get("a").get("b").get("c")[2].get("d").get("e"))