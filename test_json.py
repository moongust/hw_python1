# Four Fundamental Forces with JSON
import json

d = {}

d["gravity"] = {
    "mediator": "gravitons",
    "relative strength": "1",
    "range": "infinity",
    "ru_description":"Универсальное фундаментальное взаимодействие между всеми материальными телами."
}
d["weak"] = {
    "mediator": "W/Z bosons",
    "relative strength": "10^25",
    "range": "10^-18",
    "ru_description":"Слабое ядерное взаимодействие, ответственное, в частности, за процессы бета-распада" +
                        " атомных ядер и слабые распады элементарных частиц"
}
d["electromagnetic"] = {
    "mediator": "photons",
    "relative strength": "10^36",
    "range": "infinity",
    "ru_description":"Электромагнитное взаимодействие между частицами, обладающими электрическим зарядом."
}
d["strong"] = {
    "mediator": "gluons",
    "relative strength": "10^38",
    "range": "10^-15",
    "ru_description":"Сильное ядерное взаимодействие, действует в масштабах порядка размера атомного ядра и менее."
}

print(d)

data = json.dumps(d, indent=1, sort_keys=True, ensure_ascii = False)    # encoding, return a string
print("\n",type(data))
print(data)

filename = "test_json_four_forces.json"
print("Write json string to file", filename)
with open(filename,"w") as f:
    f.write(data)

print("Load from file", filename)
with open(filename) as f:
    data2 = f.read()
d2 = json.loads(data2)

print(data2)
print("\n")
print(d2)
print(d2==d)


# Вариант с записью-чтением прямо в файл
# write to a file
# with open("4forces.json","w") as f:
#  json.dump(d, f)
# reads it back
#with open("4forces.json","r") as f:
#  d = json.load(f)




