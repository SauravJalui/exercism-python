# class HighScores:
# 	def __init__(self):
# 		self.scores = scores

# 	def latest(self):
# 	    return self.scores[-1]

# 	def personal_best(self):
# 	    return max(self.scores)

# 	def personal_top_three(self):
# 	    return sorted(self.scores, reverse = True)[0:3]

# to pass the tests had to use the below:
scores = []
def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores, reverse = True)[0:3]
