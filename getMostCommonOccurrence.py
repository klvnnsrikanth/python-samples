import operator

#Hasing key is char and value is count

def char_count_dict(string):
        char_count = {} #Map each char to its count
        for char in string:
                if char in char_count:
                        char_count[char] = char_count[char] + 1
                else:
                        char_count[char] = 1
        return char_count


def MostCommonChar(str, num): 
	char_count = char_count_dict(str) # returns each char to its count dictionary 
	print char_count
	sorted_x = sorted(char_count.iteritems(), key=operator.itemgetter(1))
	print sorted_x
	print sorted_x[-num][0]

MostCommonChar("Aabra Ka Daabra", 2)
MostCommonChar("Aabra Ka Daabra", 1)
MostCommonChar("Aabra Ka Daabra", 3)
MostCommonChar("Aabra Ka Daabra", 5)
