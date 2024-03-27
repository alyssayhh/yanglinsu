def extract_subject(sentence):
    ga_index = sentence.find("が")

if ga_index != -1:
    subject = sentence[:ga_index].strip()
else:
    subject = "No subject found"
return subject

# test case

sentence = [
    "猫が魚を食べる",
    "彼女が花を買う",
    "子供たちが公園で遊ぶ",
    "本を読む",
    "泳ぐ",
    "日本語を勉強する" 
]
for sentence in i:
    subject = extract_subject(i)
    print("Sentence:", i)
    print("Subject:", i)
    print()  # Print an empty line for better readability

