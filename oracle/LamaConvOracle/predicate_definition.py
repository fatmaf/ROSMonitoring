#so this is just a class i'm using 
#so i dont have to copy paste stuff 
# and i can just re use the same thing 


class PredicateDefinition(object):
	
	def __init__(self,do_loc,do_rad,locs,property):
		self.rad_preds = {'dangerred':'danger_red', 'dangerorange':'danger_orange'}
		self.locs = locs 
		self.predicates = dict(time = 0)
		self.do_loc = do_loc
		if do_loc:
			for loc in self.locs:
				self.predicates[loc] = False 
				
		self.do_rad = do_rad 
		if do_rad:
			for pred in self.rad_preds:
				self.predicates[pred] = False
				
		self.property = property
			
	
	def process_message_at(self,message):
		if message['topic'] == 'at_location':
			for loc in locs:
				if message['data'] == loc:
					self.predicates[loc] = True 
				else:
					self.predicates[loc] = False


	def process_message_radiation(self,message):
		if message['topic'] == 'radiation_status':
			for rpred in self.rad_preds:
				if message['data'] == self.rad_preds[rpred]:
					self.predicates[rpred]=True
				else:
					self.predicates[rpred]=False 
					
	def process_message(self,message):
		if self.do_loc:
			self.process_message_at(message)
		if self.do_rad:
			self.process_message_radiation(message)
		self.predicates['time'] = message['time']
		return self.predicates
					
	
