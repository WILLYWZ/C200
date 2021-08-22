def what(chevy, gmc, cadillac, buick):
	temp1 = who(chevy, cadillac)
	temp1 * cadillac
	temp1 = temp1 * buick
	return temp1


def who(cat, dog):
	temp1 = "Abra"
	if type(cat) == str:
		temp1 = cat * dog
	elif type(cat) == float:
		temp1 = str(temp1) + " is evolving"
	elif type(cat) == list:
		temp1 = "Bayleef"
	else:
		temp1 = dog * cat
	where()
	return temp1

def where():
	temp1 = "Good News Everyone"
	temp1 = temp1[2:6]
	temp1 = temp1 + "ama"
	return temp1

print(what("a", 1, 2, 3))
print(what(1.0, 1, 1, 1))
print(where())
