file = open("hamlet.txt","r")

word_counts = {}

frequent_words = ["the", "a", "and", "of", "to"]

for line in file:
    for word in line.split():

        if word in frequent_words:
            continue

        if word in word_counts:
            word_counts[word] = word_counts[word] + 1

        else:
            word_counts[word] = 1

allPairs = iter((word_counts.items()))
firstPair = next(allPairs)

mostFrequent = firstPair[0]
print(mostFrequent)
for word in word_counts:
    if word_counts[word] > word_counts[mostFrequent]:
        mostFrequent = word

print(" \n \nThe most frequent word is:", mostFrequent," \n \nIt appears", word_counts[mostFrequent] ,"times!!!")