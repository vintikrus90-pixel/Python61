employees = {}

employees[(1, "Alice")] = {"position": "Manager", "skills":{"leadership", "communication"}}
employees[(2, "Bob")] = {"position": "Developer", "skills":{"python", "databases"}}

for (id, name), info in employees.items():
    print(f"Сотрудник {id}: {name}")
    print(f"Должность : {info['position']}")
    print(f"Навыки : {', '.join(info['skills'])}")


projects = {}

projects[(101, "Project Alpha")] = {"participants" : {"Alice" : "Lead", "Bob" : "Developer"}}
projects[(102, "Project Beta")] = {"participants" : {"Charlie" : "Manager", "Dave" : "Analyst"}}

for(id, title), details in projects.items():
    print(f"Проект {id}: {title}")
    for name, role in details["participants"].items():
        print(f"{name}  - {role}")