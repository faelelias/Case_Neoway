
#!/usr/bin/env python
# -- coding: utf-8 --

## higienização dos dados
accents = {"Ú":"U","Ê":"E","É":"E"}

with open("base_new") as f:
    res = f.read()
for k, v  in accents.items():
    if k in res:
        res = res.replace(k, v)

res = res.lower()
res= res.split(" ")
print(res)




