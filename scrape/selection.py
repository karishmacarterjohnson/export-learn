def choose_units(hierarchy):
    i = 1
    hierarchy_keys = {}
    for unit in hierarchy:
        hierarchy_keys[i] = unit
        i += 1

    remove = [unit for unit in hierarchy]
    cont = True
    while cont:
        print("the following units are available to save")
        for key, unit in hierarchy_keys.items():
            print("\t", key, ":", unit)
        value = input("enter the number of the unit to download or 'x' to start downloads\n")
        if value.lower() == 'x':
            cont = False
        try:
            unit_selected = hierarchy_keys.get(int(value))
            remove.remove(unit_selected)
            hierarchy_keys.pop(int(value))
        except:
            pass
    
    for unit in remove:
        hierarchy.pop(unit)
    print("your downloads will start now! please be patient :)")

def make_selection(hierarchy):
    decision = False
    while not decision:
        select = input("enter 'a' to download all or 's' to select specific units\n")
        if select.lower() == 'a':
            decision = True
        elif select.lower() == 's':
            choose_units(hierarchy)
            decision = True
