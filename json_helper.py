import json
import os
import pickle





def read_json(x):
    with open(x,'r') as f:
        data = json.load(f)
    return data

#print(read_json('data/super_smash_bros/mario.json'))

def read_all_json_files(rootdir):

    alldicts = []
    dir_name = '.'

    for root, dirs, files in os.walk(rootdir):
        for name in files:
            if name.endswith((".json")):
                #print(read_json(full_path))
                full_path = os.path.join(root, name)
                #print(full_path)
                #print(read_json(full_path))
                alldicts.append(read_json(full_path))
    return alldicts

print(read_all_json_files('data'))
test_object = read_all_json_files('data')


#super_smash_characters.pickle.

def write_pickle(filename, objectstoserialize):
    with open(filename, 'wb') as f:
        pickle.dump(objectstoserialize, f)

write_pickle('super_smash_characters.pickle', test_object)



def load_pickle(filename):
    with open(filename, 'rb') as f:
        return  pickle.load(f)

print(load_pickle('super_smash_characters.pickle'))





