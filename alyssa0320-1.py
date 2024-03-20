def extract_subjects(sentences):
    subjects = []
    for sentence in sentences:
        ga_index = sentence.find("が")
        subject = sentence[:ga_index].strip()
        subjects.append(subject)
    return subjects

sentences = ["私（わたし）がリンゴを食べます","彼（かれ）が本を読みます", "あなたが手紙を書きます"]
subjects = extract_subjects(sentences)
print("Subjects:", subjects)

