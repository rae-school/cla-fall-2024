import markovify

a = open("sonnets-short.txt").read()
b = open("cla.txt").read()
generator_a = markovify.Text(a)
generator_b = markovify.Text(b)
combo = markovify.combine([generator_a, generator_b], [0.4, 0.6])

sonnet = ""
for i in range(14):
    line = str(combo.make_short_sentence(60, tries=100))
    sonnet += line
    sonnet += "\n"

print(sonnet)