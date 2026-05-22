import os, re

base = '.'
fixed = []

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Fix ** TEXT -> **TEXT (bold with leading space)
        new_content = re.sub(r'\*\* +', '**', content)
        # Also fix TEXT ** -> TEXT** (trailing space before closing **)
        new_content = re.sub(r' +\*\*', '**', new_content)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            fixed.append(path.replace('./', ''))

print(f'Fixed {len(fixed)} files:')
for ff in fixed:
    print(f'  - {ff}')
