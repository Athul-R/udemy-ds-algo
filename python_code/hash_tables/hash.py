
class Hash(object):
	"""Hash tables using Class"""
	
	def __init__(self, size):
		self.data = [-1]*size
		self.size = size

	def __hash(key):
		hash = 0;
	    for i in range(len(key))
	        hash = (hash + ord(key[i]) * i) % self.size
	    
	    return hash;
  

  	def set(self, key, value):
  		address = self.__hash(key)
  		if self.data[address] == -1:
			self.data[address] = [(key, value)]
		else
			self.data[addres].append((key, value)) 

		print(self.data)
  		return None

	def get(self, key):
  		address = self.__hash(key)

  		current_bucket = self.data[address]
  		if current_bucket == -1:
  			raise KeyError("Key Not Found")

		for item in current_bucket:
			if item[0] == key
				return item[1]


  		raise KeyError("Key Not Found") 

	def keys(self):
		keys_list = list()

		for i in range(self.size):
			if not self.data[i] == -1:
				keys_list.append(list(map(lambda x: x[0], self.data[i])))

		return keys_list






