# prepare the input:
replacements = {}
replacements_p2 = {}
with open("src/day19.txt") as f:
    for line in f:
        line = line.split()
        if not line:
            break
        if line[0] in replacements:
            replacements[line[0]].append(line[2])
        else:
            replacements[line[0]] = [line[2], ]
            
        replacements_p2[line[2]] = line[0]
    mol = f.read().strip()

#part 1:
#making the replacements:
molecules = []
for i, c in enumerate(mol):
    if c in replacements:
        for r in replacements[c]:
            molecules.append(mol[:i] + r + mol[i+1:])
    if i != len(mol)-1 and mol[i:i+2] in replacements:
        for r in replacements[mol[i:i+2]]:
            molecules.append(mol[:i] + r + mol[i+2:])   
print("the answer for part 1:", len(set(molecules)))

#part 2:
mol2 = mol[:]
rep_values = sorted(list(replacements_p2.keys()), key=len, reverse=True)
non_overlaps = []
cntr = 0
is_changed = True
while is_changed:
    is_changed = False
    for r in rep_values:
        if r in mol2:
            mol2 = mol2.replace(r, replacements_p2[r], 1)
            cntr += 1
            is_changed = True
    
print("the answer for part 2: ", cntr)