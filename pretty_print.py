import json
import pprint

my_mapping = {'a': 22, 'b': 44, 'c': 0xc0ffee}
print(my_mapping)

print(json.dumps(my_mapping, indent=4, sort_keys=True))


stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
print(stuff)
print()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
