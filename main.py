from scrape.module import *
from scrape.unit import *
from scrape.login import *
from scrape.selection import *
import os


driver = login(os.getcwd())
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

hierarchy = get_units(driver)

make_selection(hierarchy)
path = os.path.join(os.getcwd(),'ada-learn')

for unit, modules in hierarchy.items():
    unit_path = os.path.join(path, unit) 
    try: 
        os.mkdir(unit_path)
    except:
        pass
    for module_name, module_link in modules.items():
        module_path = os.path.join(unit_path, module_name)
        os.mkdir(module_path)
        driver = save_pages(module_path, module_link, driver)
    print(f"{unit} has been saved!")
driver.close()
driver.quit()

 
# ask zip or leave as is
# if input().lower() == y:
# zip
