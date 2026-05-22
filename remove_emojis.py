import os, re

# Match common emoji ranges
emoji_pattern = re.compile(
    '['
    '\U0001F000-\U0001FFFF'  # symbols & pictographs
    '\U0001F300-\U0001F9FF'  # emoji
    '\U00002600-\U000026FF'  # misc symbols
    '\U00002700-\U000027BF'  # dingbats
    '\U0001F100-\U0001F1FF'  # enclosed chars
    '\U0001F200-\U0001F2FF'  # enclosed ideographs
    '\U0001F600-\U0001F64F'  # emoticons
    '\U0001F680-\U0001F6FF'  # transport
    '\U0001F900-\U0001F9FF'  # supplemental
    '\U0000FE00-\U0000FE0F'  # variation selectors
    '\U0000200D'             # zero-width joiner
    '\ufe0f'                 # variation selector-16
    ']',
    re.UNICODE
)

base = '.'
fixed_files = []

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        new_content = emoji_pattern.sub('', content)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            fixed_files.append(path.replace('.\\', ''))

print(f'Fixed {len(fixed_files)} files:')
for ff in fixed_files:
    print(f'  - {ff}')
