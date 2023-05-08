import json
import os

str2curve_form = {
    "Weierstrass": "WEIERSTRASS",
    "Montgomery": "MONTGOMERY",
    "TwistedEdwards": "TWISTED_EDWARDS",
    "Edwards": "EDWARDS"
}


def process(curves):
    print(f"// Category: {curves['name']}")
    print(f"// {curves['desc']}")

    for c in curves['curves']:
        aliases = ', '.join(f"\"{i}\"" for i in c.get('aliases', []))
        f_type = c['field']['type'].upper()
        if c['desc'] != "":
            print(f"// {c['desc']}")
        print(
            f"{{\"{c['name']}\", {{{aliases}}}, CurveForm::{str2curve_form[c['form']]}, FieldType::{f_type}, {int(c['field']['bits'] / 2)}}},")
    print()


if __name__ == '__main__':
    for f in os.listdir("."):
        if os.path.isfile(f):
            continue

        jsonf = os.path.join(f, "curves.json")
        if not os.path.exists(jsonf):
            continue

        with open(jsonf) as f_obj:
            process(json.load(f_obj))
