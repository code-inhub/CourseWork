
import re

# Given poem
poem = '''If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.'''

count_v = len(re.findall(r'v', poem))
print(f"Number of times 'v' appears in the poem: {count_v}")

poem_single_line = re.sub(r'\n', ' ', poem)
print("\nPoem in a single line:")
print(poem_single_line)


modified_poem = re.sub(r'ch', 'Ch', poem)
modified_poem = re.sub(r'co', 'Co', modified_poem)
print("\nPoem with 'ch' or 'co' replaced with 'Ch' or 'Co':")
print(modified_poem,end="\n\n")

poem_modified = re.sub(r'ai.{3}', 'ai*\*', poem)
poem_modified = re.sub(r'hi.{3}', 'hi*\*', poem_modified)
print(poem_modified)