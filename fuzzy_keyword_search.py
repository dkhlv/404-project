import csv
import hashlib
from cryptography.fernet import Fernet

# This project demonstrates searchable encryption method based on fuzzy keyword search
# Workflow is based on 2010 paper "Fuzzy Keyword Search over Encrypted Data in Cloud Computing" by Li et al. 

# Return a set of fuzzy keywords for a given word
# Default edit distance is 1
# TO DO: customize edit distance
def build_fuzzy_keyword_set(word):
	fuzzy_keys = []
	fuzzy_keys.append("*" + word)
	for i in range(len(word)+1):
		pattern = word[:i] + "*" + word[i+1:]
		fuzzy_keys.append(pattern)
	return fuzzy_keys

# Apply trapdoor function (substituted with SHA-256 hash) to all given fuzzy keywords 
def build_trapdoor_set(fuzzy_keys):
	hashed_fuzzy_keys = []
	for word in fuzzy_keys:
		m = hashlib.sha256()
		m.update(str.encode(word))
		hashed_fuzzy_keys.append(m.digest())
	return hashed_fuzzy_keys

# seach index table for all fuzzy matches
def search(index, query):
	results = []
	for keyword in query:
		if keyword in index.keys():
			results = index[keyword]
	return results

def update_table(index, ct):
	if key in index.keys():
		index[key].append(ct)
	else:
		index[key] = [ct]
	return index

def write_to_file(index):
	with open('index.csv', 'w') as f:
		for key in index.keys():
			f.write("{},{}\n".format(key,index[key]))

# Step 1 - Build encrypted index table and store as csv file

# In the index table keys are hashed fuzzy matches for every keyword
# Values are encrypted keywords + file IDs

secret_key = Fernet.generate_key() # Secret key that only user knows but server doesn't
cipher_suite = Fernet(secret_key) # Choose encryption method to be Fernet
index = {}

with open('unencrypted_data.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		keywords = row['keywords'].split()
		for word in keywords:
			fuzzy_keys = build_fuzzy_keyword_set(word)
			hashed_fuzzy_keys = build_trapdoor_set(fuzzy_keys)
			for key in hashed_fuzzy_keys:
				plaintext = word + "," + row['fid']
				ciphertext = cipher_suite.encrypt(str.encode(plaintext))
				index = update_table(index, ciphertext)
	write_to_file(index)


# Step 2 - Simulate User query

query = input('Enter your query:  ')
#query = 'machine'

# Apply trapdoor function on all fuzzy matches of a given query
fuzzy_keys = build_fuzzy_keyword_set(query)
encrypted_query = build_trapdoor_set(fuzzy_keys)

print("\nA set of fuzzy keywords: ")
print(fuzzy_keys)

# Step 3 - Server compares encrypted query keywords with index table and returns results

print("\nSearching for results...")
results = search(index, encrypted_query)
if len(results)==0:
	print("No results")
else:
	print("\nServer returned these encrypted file identifiers:\n")
	print(results)

# Step 4 - User decrypts results

decrypted_results = []
for ct in results:
	decrypted_results.append(cipher_suite.decrypt(ct))

print("\nDecrypted file identifiers:\n")
print(decrypted_results)

# Step 5 - User retrieves relevant files given file IDs

# get a set of file ids
fids = set()
for result in decrypted_results:
	result = result.decode("utf-8")
	fid = result.split(',')[-1]
	fids.add(fid)
print('\n\nHere are the results that match your query "{}":\n'.format(query))

#retrieve paper titles that match file ids
with open('unencrypted_data.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['fid'] in fids:
			print(row['title'])
		









