#!/usr/bin/env python3

import argparse
import lxml.etree as ET


lines = ['import openmc', '', 'mats = openmc.Materials()', '']

parser = argparse.ArgumentParser()
parser.add_argument('matfile')
args = parser.parse_args()

tree = ET.parse(args.matfile)
root = tree.getroot()

for material in root.findall('material'):
    mat_id = material.attrib['id']
    lines.append(f"mat = openmc.Material({mat_id})")

    # Try to determine name for material
    prev = material.getprevious()
    if prev is not None:
        if prev.tag is ET.Comment:
            if '\n' not in prev.text:
                lines.append(f'mat.name = "{prev.text.strip()}"')

    for child in material:
        if child.tag == 'density':
            units = child.attrib['units']
            value = child.get('value')
            if value is not None:
                lines.append(f"mat.set_density('{units}', {value})")
            else:
                lines.append(f"mat.set_density('{units}')")
        elif child.tag in ('nuclide', 'element'):
            name = child.attrib['name']
            name = name.replace('-', '')
            name = name.replace('Nat', '0')
            if child.tag == 'nuclide' and name.endswith('m'):
                name = name[:-1] + '_m1'
            if 'ao' in child.attrib:
                pct = child.get('ao')
                lines.append(f"mat.add_{child.tag}('{name}', {pct})")
            else:
                assert 'wo' in child.attrib
                pct = child.get('wo')
                lines.append(f"mat.add_{child.tag}({name}, {pct}, 'wo')")
    lines.append('mats.append(mat)')
    lines.append('')

lines.append('mats.export_to_xml()')
lines.append('')

with open('generate_materials.py', 'w') as fh:
    fh.write('\n'.join(lines))
