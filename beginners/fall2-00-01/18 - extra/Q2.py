sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


print(sampleDict.get("class", {}).get("student", {}).get("marks", {}).get("history"))