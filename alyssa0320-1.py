def extract_subject(sentence):
    'wo_index' = sentence.find("を")

if wo_index != -1:
    subject = sentence[:wo_index].strip()
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
for sentence in sentences:
    subject = extract_subject(sentence)
    print("Sentence:", sentence)
    print("Subject:", subject)
    print()  # Print an empty line for better readability

