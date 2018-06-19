import sanitize_inputs as si

'''(1) add concept
(2) add category
(3) edit concept'''

class category():
    def __init__(self, name):
        self.ser = 0
        #assign a serial number that is persistant so that name can be changed.
        self.name = name

    def set_score(self, score):
        self.score = score
        
class concept():
    def __init__(self, name):
        self.ser = 0 
        self.name = name
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)
        
class matrix():
    def __init__(self):
        self.next_concept = 0 # initialize the serial numbers for concepts
        self.next_category = 0 # initialize the serial numbers for categories
        self.concept_list = []
        self.category_list = []
        
    def new_concept(self, name):
        self.concept_list.append(concept(name, self.next_concept))
        self.next_concept += 1
        for c in self.category_list:
            self.concept_list[-1].add_category(c)

    def new_category(self, name):
        self.category_list.append(category(name, self.next_category))
        self.next_category += 1
        for c in self.concept_list:
            c.add_category(self.category_list[-1])
            
