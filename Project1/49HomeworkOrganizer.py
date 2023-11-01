class Assignment:
  def __init__ (self, name, added, due, importance):
    self.name = name
    self.added = added
    self.due = due
    self.importance = importance
  def getName(self):
    return self.name
  def getAdded(self):
    return self.added
  def getDue(self):
    return self.due
  def getImportance(self):
    return self.importance

ans = "0"
assignments = []
while ans!="":
  ans = input("assign, unassign or view assignment: ")
  if ans == "assign":
    name = input("Assignment name: ")
    added = input("Date added: ")
    due = input("Due date: ")
    importance = input("On a scale from 1 to 10, how important is it: ")
    assignments.append(Assignment(name, added, due, importance))
  elif ans == "unassign":
    name = input("which assignment do you want to anassign: ")
    for i in assignments:
      if i.name == name:
        assignments.remove(i)
  elif ans == "view":
    for i in assignments:
      print(i.name)
    print("How do you want it viewed?")
    viewed = input("alphabetically, date, due, or importance: ")
    if viewed == "alphabetically":
      assignments.sort(key=Assignment.getName)
      for i in assignments:
        print(i.name)
    elif viewed == "date":
      assignments.sort(key=Assignment.getAdded)
      for i in assignments:
        print(i.name, i.added)
    elif viewed == "due":
      assignments.sort(key=Assignment.getDue)
      for i in assignments:
        print(i.name, i.due)
    elif viewed == "importance":
      assignments.sort(reverse=True, key=Assignment.getImportance)
      for i in assignments:
        print(i.name, i.importance)
    else:
      print("not an option")
  else:
    print("not an option")