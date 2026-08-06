import h5py

f = h5py.File('model/plant_disease_transfer.h5', 'r')
print('Model attributes:')
for key, value in f.attrs.items():
    print(f'  {key}: {value}')

print('\nTop level structure:')
def print_structure(name, obj):
    print(f'  {name}: {type(obj).__name__}')
f.visititems(print_structure)
f.close()
