brthday = {
    "Chetan": "30-06-2024",
    "Chandan": "27-08-2007",
    "virat": "05-10-1988",
}
print(brthday.get("Chetan", "Not found"))
print(brthday.get("Sudeep", "Not found"))

brthday["sudeep"] = "02-09-1973"
print(brthday.get("sudeep", "not found"))

#upadating...
brthday["Chetan"] = "30-05-2005"

brthday.pop("virat")
print(brthday)

print(brthday.keys())
print(brthday.values())
print(brthday.items())

del brthday["sudeep"]
print(brthday)