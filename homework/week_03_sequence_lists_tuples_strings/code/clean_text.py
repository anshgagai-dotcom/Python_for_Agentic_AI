#sentence = " I     Love Python      Too Much"
sentence = " I     am learning     python    programing     language    ."


raw_data = sentence.split(" ")

words = []
for text in raw_data:
    if text:
        words.append(text)

clean_data = " ".join(words)

clean_data = clean_data.replace(" .", "")

print(" Dirty Data: ", sentence)

print(" Clean Data: ", clean_data)
