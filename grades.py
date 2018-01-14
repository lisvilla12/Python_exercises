import random
def gradeScore():
    for x in range(10):
        random_num = random.randint(60,100)
        if random_num <= 69:
            print "Score:", random_num, "; Your grade is D"
        elif random_num <= 79:
            print "Score:", random_num, "; Your grade is C"
        elif random_num <= 89:
            print "Score:", random_num, "; Your grade is B"
        elif random_num <= 100:
            print "Score:", random_num, "; Your grade is A"

gradeScore()