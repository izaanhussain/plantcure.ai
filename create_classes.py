import os
import pickle

train_dir = r"C:\Users\hp\Downloads\archive\New Plant Diseases Dataset(Augmented)\New Plant Diseases Dataset(Augmented)\train"

class_indices = {}
classes = sorted(os.listdir(train_dir))
for idx, class_name in enumerate(classes):
    class_indices[class_name] = idx

with open("class_indices.pkl", "wb") as f:
    pickle.dump(class_indices, f)

print("class_indices.pkl saved!")
print(class_indices)
