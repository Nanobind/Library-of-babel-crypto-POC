s = 'long string that I want to split up'
indices = [3,6,12,17]
parts = [s[i:j] for i,j in zip(indices, indices[1:]+[None])]

print(parts)