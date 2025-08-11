import os
import glob
import xml.etree.ElementTree as ET
import sys

def set_working_directory_to_script_location():
    # Make sure we're running in the same folder as the script, even if double-clicked
    script_path = os.path.abspath(sys.argv[0])
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    print(f"Working directory set to script location: {script_dir}")

def get_input_files():
    xml_file = None
    classnames_file = None
    # Detect types.xml or classnames file in current directory
    for f in os.listdir('.'):
        if f.lower() == 'types.xml':
            xml_file = f
        elif 'classname' in f.lower() and f.lower().endswith(('.txt', '.csv')):
            classnames_file = f
    print("Files in current directory:", os.listdir('.'))
    if xml_file:
        print("Detected types.xml:", xml_file)
    if classnames_file:
        print("Detected classnames file:", classnames_file)
    return xml_file, classnames_file

def parse_types_xml(xml_file):
    # Parse types.xml to extract classnames and usage info
    classnames = []
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for item in root.findall('type'):
            name = item.get('name')
            nominal = item.findtext('nominal')
            classnames.append({'name': name, 'nominal': nominal})
    except Exception as e:
        print(f"Error parsing XML: {e}")
    return classnames

def parse_classnames_txt(classnames_file):
    # Read classnames from txt/csv file (one per line)
    classnames = []
    try:
        with open(classnames_file, encoding='utf-8') as f:
            for line in f:
                name = line.strip()
                if name:
                    classnames.append({'name': name, 'nominal': None})
    except Exception as e:
        print(f"Error reading classnames file: {e}")
    return classnames

def prompt_output_format():
    print("Choose output format:")
    print("1. Dr. Jones")
    print("2. Trader Plus")
    print("3. Expansion Markets")
    while True:
        sel = input("Enter 1, 2, or 3: ").strip()
        if sel in {"1", "2", "3"}:
            return int(sel)

def prompt_output_file(default):
    out_file = input(f"Enter output filename (default: {default}): ").strip()
    if not out_file:
        out_file = default
    if not os.path.isfile(out_file):
        open(out_file, 'w', encoding='utf-8').close()
        print(f"Created new file: {out_file}")
    return out_file

def to_drjones_format(classnames):
    # Dr. Jones: classname,0,1,-1,-1,0,0
    lines = []
    for item in classnames:
        lines.append(f"{item['name']},0,1,-1,-1,0,0")
    return '\n'.join(lines)

def to_traderplus_format(classnames):
    # Trader Plus: classname,price,stock,minStock,maxStock,category
    lines = []
    for item in classnames:
        lines.append(f"{item['name']},100,10,1,100,Category")
    return '\n'.join(lines)

def to_expansion_format(classnames):
    # Expansion Market: JSON-like
    items = []
    for item in classnames:
        items.append(f'    {{ "ClassName": "{item["name"]}", "MinPriceThreshold": 100, "MaxPriceThreshold": 500, "SellPricePercent": 50, "MaxStockThreshold": 100, "MinStockThreshold": 1 }}')
    return '[\n' + ',\n'.join(items) + '\n]'

def main():
    print("DayZ Trader Converter\n")
    set_working_directory_to_script_location()
    xml_file, classnames_file = get_input_files()

    if not xml_file and not classnames_file:
        print("No types.xml or classnames file found in current folder.")
        input("Press Enter to exit...")
        return

    # Prefer types.xml if both exist
    classnames = []
    if xml_file:
        print(f"Found {xml_file}, parsing...")
        classnames = parse_types_xml(xml_file)
    elif classnames_file:
        print(f"Found {classnames_file}, parsing...")
        classnames = parse_classnames_txt(classnames_file)

    # Remove classnames with empty names
    classnames = [c for c in classnames if c['name']]

    if not classnames:
        print("No classnames found in file(s).")
        input("Press Enter to exit...")
        return

    fmt = prompt_output_format()
    default_out = {1: 'DrJones.txt', 2: 'TraderPlus.txt', 3: 'ExpansionMarket.json'}[fmt]
    out_file = prompt_output_file(default_out)

    if fmt == 1:
        output = to_drjones_format(classnames)
    elif fmt == 2:
        output = to_traderplus_format(classnames)
    elif fmt == 3:
        output = to_expansion_format(classnames)

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"\nDone! Output written to {out_file}")
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()