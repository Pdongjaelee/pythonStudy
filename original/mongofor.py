import ifcopenshell
import ifcopenshell.util.element

JEONJU_FILE_PATH =


model = ifcopenshell.open(JEONJU_FILE_PATH)

all_type = model.wrapped_data.types()
print(all_type)