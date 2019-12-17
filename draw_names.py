import random

class person:
  def __init__(self, name, spouse, last_year):
    self.name = name
    self.spouse = spouse
    self.last_year = last_year

name_list = []

f = open("names.txt")
for l in f:
  l = l.split()
  if(len(l) >2):
    name_list.append(person(l[0], l[1], l[2]))
  else:
    name_list.append(person(l[0], l[1], None))



failure = True
total_tries = 0
while failure == True:
  failure = False
  drawn = []
  for p in name_list:
    found_val = 0
    tries = 0
    while(found_val == 0 and tries < 20):
      tries += 1
      num = random.randint(0, len(name_list) - 1)
      if (p.name != name_list[num].name and p.spouse != name_list[num].name and p.last_year != name_list[num].name and name_list[num].name not in drawn):
        p.drawn = name_list[num].name
        drawn.append(name_list[num].name)
        found_val = 1
    if found_val == 0:
      failure = True
      break
  total_tries += 1
  if(total_tries > 20): 
    break


for p in name_list:
    print (p.name + " has " +  p.drawn)
