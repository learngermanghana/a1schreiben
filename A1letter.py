import streamlit as st
import re
import random

st.set_page_config(page_title="A1 Schreiben Trainer", page_icon="✉️")

st.title("✉️ A1 Schreiben Trainer")
st.write("**Learn Language Education Academy** – Letter Writing Practice for A1 Exam")

student_name = st.text_input("Please enter your name:")
pledge = st.checkbox("✅ I promise to write my own letter and not overuse translators.")

if not student_name or not pledge:
    st.warning("Please enter your name and accept the pledge before continuing.")
    st.stop()

st.success(f"Welcome, {student_name}! You may now begin.")

letter_tasks = {
    1: {"task": "Schreiben Sie eine E-Mail an Ihren Arzt und sagen Sie Ihren Termin ab.",
        "points": ["Warum schreiben Sie?", "Sagen Sie: den Grund für die Absage.", "Fragen Sie: nach einem neuen Termin."]},
    2: {"task": "Schreiben Sie eine Einladung an Ihren Freund zur Feier Ihres neuen Jobs.",
        "points": ["Warum schreiben Sie?", "Wann ist die Feier?", "Wer soll was mitbringen?"]},
    3: {"task": "Schreiben Sie eine E-Mail an einen Freund und teilen Sie ihm mit, dass Sie ihn besuchen möchten.",
        "points": ["Warum schreiben Sie?", "Wann besuchen Sie ihn?", "Was möchten Sie zusammen machen?"]},
    4: {"task": "Schreiben Sie eine E-Mail an eine Kochschule und melden Sie sich für einen Kochkurs an.",
        "points": ["Warum schreiben Sie?", "Wann beginnt der Kurs?", "Wie viel kostet der Kurs?"]},
    5: {"task": "Schreiben Sie eine E-Mail an die Sprachschule 'All About Deutsch' in Berlin.",
        "points": ["Wann möchten Sie den Kurs machen?", "Informationen zum Wohnen/Wohnheim.", "Fragen Sie nach Terminen und Preisen."]},
    6: {"task": "Schreiben Sie eine E-Mail an die Bibliothek und fragen Sie, ob Sie ein reserviertes Buch abholen können.",
        "points": ["Warum schreiben Sie?", "Wann können Sie das Buch abholen?", "Wie lange dürfen Sie es behalten?"]},
    7: {"task": "Schreiben Sie eine Einladung zu einer Geburtstagsparty.",
        "points": ["Wo ist die Party?", "Wann ist die Party?", "Wer soll was mitbringen?"]},
    8: {"task": "Ihre Freundin Petra will Sie im Juni besuchen. Schreiben Sie an Petra.",
        "points": ["Sie müssen im Juni nach Frankfurt.", "Bitte: Petra soll im August kommen.", "Sie haben am 11.8. Geburtstag."]},
    9: {"task": "Schreiben Sie eine E-Mail an die Wohnungs-Agentur 'Haussuche' in München.",
        "points": ["Sie suchen ein Apartment für drei Monate.", "Sie wollen einen Kurs besuchen.", "Ankunft Anfang Juni."]},
    10: {"task": "Sie wollen nach Berlin fahren. Schreiben Sie eine E-Mail an die Touristeninformation.",
         "points": ["Wann besuchen Sie Berlin?", "Fragen Sie nach Hotelpreisen oder Jugendherberge.", "Fragen Sie nach Sehenswürdigkeiten."]},
    11: {"task": "Schreiben Sie eine E-Mail an Ihren Arzt und fragen Sie nach einem Termin.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: wann der früheste Termin möglich ist.", "Fragen Sie: welche Unterlagen Sie mitbringen sollen."]},
    12: {"task": "Schreiben Sie eine E-Mail an einen Freund und laden Sie ihn ein, Sie in Ihrer Stadt zu besuchen.",
         "points": ["Warum schreiben Sie?", "Wann kann er kommen?", "Kann er bei Ihnen übernachten?"]},
    13: {"task": "Schreiben Sie eine E-Mail an einen Freund und sagen Sie Ihren geplanten Besuch ab.",
         "points": ["Warum absagen?", "Entschuldigen Sie sich.", "Neuen Termin vorschlagen."]},
    14: {"task": "Schreiben Sie eine Entschuldigung an die Lehrerin von Ihrem Sohn.",
         "points": ["Ihr Sohn kann nicht in die Schule gehen.", "Grund: Warum?", "Sie kommen morgen wegen der Hausaufgaben."]},
    15: {"task": "Schreiben Sie eine E-Mail an ein Geschäft und reklamieren Sie ein gekauftes Produkt.",
         "points": ["Warum schreiben Sie?", "Beschreiben Sie das Problem.", "Fragen Sie nach Rückgabe oder Umtausch."]},
    16: {"task": "Schreiben Sie eine E-Mail an Ihre Freundin. Sie kommen zur Party später.",
         "points": ["Entschuldigen Sie sich.", "Information über Ihre Besprechung.", "Fragen Sie, ob sie Hilfe braucht."]},
    17: {"task": "Schreiben Sie eine E-Mail und gratulieren Sie einem Freund zu seinem neuen Job.",
         "points": ["Glückwunsch zum Job.", "Fragen Sie, wie der neue Job ist.", "Vorschlag: gemeinsam feiern."]},
    18: {"task": "Sie möchten Sachsen besuchen. Schreiben Sie an die Touristeninformation.",
         "points": ["Wann besuchen Sie Sachsen?", "Fragen Sie nach Sehenswürdigkeiten.", "Fragen Sie nach Hotels oder Gästehäusern."]},
    19: {"task": "Schreiben Sie eine E-Mail an ein Yogastudio und melden Sie sich für einen Kurs an.",
         "points": ["Warum schreiben Sie?", "Wann beginnt der Kurs?", "Wie lange dauert der Kurs?"]},
    20: {"task": "Sie sind krank. Sie können nicht nach Bayern zum Verlag Prax kommen.",
         "points": ["Entschuldigung.", "Neuen Termin vorschlagen.", "Wann?"]},
    21: {"task": "Schreiben Sie eine E-Mail an Frau Müller und reservieren Sie ein Zimmer.",
         "points": ["Warum schreiben Sie?", "Fragen Sie nach dem Preis.", "Sagen Sie Ihre Ankunftszeit."]},
    22: {"task": "Schreiben Sie eine E-Mail an ein Restaurant und reservieren Sie einen Tisch.",
         "points": ["Warum schreiben Sie?", "Für wie viele Personen?", "Wann möchten Sie reservieren?"]}
}

task_number = st.number_input(
    "Choose a Schreiben task number (1 to 22):",
    min_value=1,
    max_value=22
)

if task_number in letter_tasks:
    st.markdown(f"### 📄 Aufgabe {task_number}: {letter_tasks[task_number]['task']}")
    st.markdown("**Please include the following points in your letter:**")
    for point in letter_tasks[task_number]['points']:
        st.markdown(f"- {point}")

student_letter = st.text_area("✏️ Write your letter here:", height=350)

def analyze_letter(letter, task_number):
    feedback = []
    score = 25

    letter = letter.strip()
    letter = letter.replace("mochte", "möchte")
    sentences = re.split(r'(?<=[.!?])\s+', letter)

    umlaut_missing = False

    common_typos = {"kostetn": "kostet", "kurz": "Kurs", "vereinbaran": "vereinbaren"}
    plural_errors = {"tag": "tage", "jahr": "jahre"}
    umlaut_words = ["möchte", "können", "müssen", "dürfen", "grüßen"]
    modal_verbs = ["möchte", "möchten", "kann", "können", "muss", "müssen", "darf", "dürfen", "soll", "sollen", "will", "wollen"]
    separable_verbs = ["mitbringen", "abholen", "vorbereiten", "ankommen"]

    polite_request_found = False
    enquiry_opening_found = False

    for sentence in sentences:
        sentence_clean = sentence.strip()
        if not sentence_clean:
            continue

        lower_sentence = sentence_clean.lower()
        words = sentence_clean.split()

        if "sehr geehrte und damen und herren" in lower_sentence:
            feedback.append("❌ Incorrect greeting. Use 'Sehr geehrte Damen und Herren'.")
            score -= 2

        if sentence_clean and sentence_clean[0].islower():
            feedback.append(f"⚠ First word should start with a capital: '{sentence_clean}'.")
            score -= 1

        for typo, correct in common_typos.items():
            if typo in lower_sentence:
                feedback.append(f"🔤 Spelling mistake: '{typo}' should be '{correct}'.")
                score -= 1

        for singular, plural in plural_errors.items():
            if singular in lower_sentence and plural not in lower_sentence:
                feedback.append(f"⚠ Did you mean '{plural}' instead of '{singular}'?")
                score -= 1

        for umlaut_word in umlaut_words:
            if umlaut_word.replace("ö", "o").replace("ü", "u").lower() in lower_sentence and umlaut_word.lower() not in lower_sentence:
                umlaut_missing = True

        if "kann ich möchte wissen" in lower_sentence:
            feedback.append("❌ 'Kann ich möchte wissen' is incorrect. Use either 'Kann ich wissen...' or 'Ich möchte wissen...', not both.")
            score -= 2

        # ✅ Smarter modal verb position check
        if lower_sentence.startswith("können wir") and lower_sentence.endswith("treffen?"):
            pass
        elif lower_sentence.startswith("ich möchte") and ("mich" in lower_sentence or "einen" in lower_sentence or "den" in lower_sentence or "die" in lower_sentence):
            pass
        else:
            if any(mv in lower_sentence for mv in modal_verbs):
                if len(words) >= 2 and words[1].lower() not in modal_verbs and not sentence_clean.endswith("?"):
                    feedback.append("⚠ Modal verb might not be at position 2.")
                    score -= 1

        # ✅ weil/denn/ob verb at end
        if any(w in lower_sentence for w in ["weil", "denn", "ob"]):
            if not lower_sentence.endswith((
                "möchte.", "möchten.", "kann.", "können.", "muss.", "müssen.", "darf.", "dürfen.",
                "soll.", "sollen.", "will.", "wollen.", "kommt.", "geht.", "zahlen.", "bezahlen."
            )):
                feedback.append("⚠ In 'weil', 'ob' or 'denn' clauses, the verb should be at the end.")
                score -= 1

        if re.search(r"ich schreibe (ihnen|dir) [a-z]", lower_sentence):
            feedback.append("⚠ You need a comma after 'Ich schreibe Ihnen' or 'Ich schreibe dir'.")
            score -= 1

        if re.search(r"ich schreibe (ihnen|dir), Weil", sentence_clean):
            feedback.append("⚠ 'weil' should be lowercase after a comma.")
            score -= 1

        if re.search(r"\b(weil|denn)\b", lower_sentence):
            if not lower_sentence.startswith(("weil", "denn")):
                if not re.search(r",\s*(weil|denn)", lower_sentence):
                    feedback.append("⚠ You need a comma before 'weil' or 'denn'.")
                    score -= 1

        if " Dir" in sentence_clean:
            feedback.append("⚠ 'Dir' should be lowercase (dir). Use 'Ihnen' for formal writing.")
            score -= 1

        if re.search(r"ich möchte wissen (wie|ob|wann)", lower_sentence):
            feedback.append("⚠ You need a comma after 'Ich möchte wissen'.")
            score -= 1

        if "ich möchte wissen wie viel kostet" in lower_sentence:
            feedback.append("⚠ Please remove 'ich möchte wissen' and just write 'Wie viel kostet ... ?'.")
            score -= 1

        for sep in separable_verbs:
            if sep in lower_sentence and not re.search(rf"{sep[:-len('bringen')]}\s+.*bringen", lower_sentence):
                feedback.append(f"⚠ Separable verb '{sep}' might not be split correctly.")
                score -= 1

        if "wie viel kostet" in lower_sentence:
            if not sentence_clean.startswith("Wie"):
                feedback.append("⚠ 'Wie viel kostet ...' must start with a capital 'Wie'.")
                score -= 1

        if "kostet" in lower_sentence or "zahlen" in lower_sentence:
            if not lower_sentence.startswith("wie viel kostet"):
                feedback.append("⚠ Please use the phrase 'Wie viel kostet ... ?' for price questions.")
                score -= 1

        if "könnten sie mir bitte" in lower_sentence and "mitteilen" in lower_sentence:
            polite_request_found = True

        if "weil ich eine anfrage stellen möchte" in lower_sentence:
            enquiry_opening_found = True

    info_words = ["preis", "stadt", "adresse", "information", "kurs"]
    if any(word in letter.lower() for word in info_words) and not polite_request_found:
        feedback.append("💡 In your body paragraph, please use a polite request: 'Könnten Sie mir bitte ... mitteilen?'")
        score -= 1

    if any(word in letter.lower() for word in info_words) and not enquiry_opening_found:
        feedback.append("💡 At the beginning of your letter, you can write: 'Ich schreibe Ihnen, weil ich eine Anfrage stellen möchte.' Then explain what you want in the next paragraph. Please ask your tutor for clarification.")
        score -= 1

    if re.search(r"ein kochkurs", letter.lower()):
        feedback.append("⚠ 'Kochkurs' is masculine. Use 'einen Kochkurs' (Akkusativ).")
        score -= 2

    if umlaut_missing:
        feedback.append("⚠ Some words may be missing umlauts (ö, ü). Example: möchte, können, Grüßen.")
        score -= 1

    # ✅ Task points check
    missing_points = []
    for point in letter_tasks[task_number]['points']:
        if "warum schreiben sie" in point.lower():
            if "weil ich eine anfrage stellen möchte" in letter.lower():
                continue
        point_keywords = [word for word in re.findall(r'\w+', point.lower())
                          if word not in ["sie", "den", "der", "das", "die", "warum", "wann", "wie", "was", "ob", "und", "oder", "mit"]]
        found = False
        for keyword in point_keywords:
            for student_word in re.findall(r'\w+', letter.lower()):
                if keyword in student_word:
                    found = True
                    break
            if found:
                break
        if not found:
            missing_points.append(point)

    if missing_points:
        feedback.append("⚠ You may have missed the following required points:")
        for mp in missing_points:
            feedback.append(f"   - {mp}")
        score -= 3

        # ✅ If 2 or more points missing → warn letter may not match
        if len(missing_points) >= 2:
            feedback.append("⚠ Your letter may not match the task you selected. Please read the question again or ask your tutor.")

    if "freue mich im voraus auf ihre antwort" not in letter.lower() and "freue mich im voraus auf deine antwort" not in letter.lower():
        feedback.append("❌ Conclusion phrase incorrect. Expected: 'Ich freue mich im Voraus auf Ihre/deine Antwort.'")
        score -= 2

    feedback.append("💡 Reminder: Check that all statements end with a full stop (.) and all questions end with a question mark (?). Start each sentence with a capital letter unless it comes after a comma.")

    return feedback, max(score, 0)

if st.button("✅ Submit Letter", key="submit_button"):
    if len(student_letter.strip()) < 20:
        st.warning("Please write a longer letter before submitting.")
    else:
        feedback, final_score = analyze_letter(student_letter, task_number)

        st.subheader("📝 Analysis & Feedback")

        if final_score >= 22:
            st.success(f"✅ Excellent! Your score: {final_score}/25")
        elif final_score >= 16:
            st.warning(f"Your score: {final_score}/25. Good attempt, but you need to improve.")
        else:
            st.error(f"Your score: {final_score}/25. You need to improve this letter.")

        st.markdown("### Feedback:")
        for item in feedback:
            st.markdown(f"- {item}")

        word_count = len(student_letter.split())
        st.markdown(f"**Your word count:** {word_count} words.")

        if word_count < 40:
            st.info("✏️ Your letter is a bit short. Aim for at least 40–60 words for A1 writing tasks.")

        st.markdown("---")

        tips = [
            "💡 No space before ? or . in German sentences.",
            "💡 Yes/No questions should start with a verb or modal verb.",
            "💡 'weil' sends the verb to the end.",
            "💡 If your sentence starts with time, the verb should be at position 2.",
            "💡 Start sentences with time or place for variety!",
            "💡 Use 'möchte' (with umlaut) not 'mochte' (past tense)."
        ]
        st.info(random.choice(tips))

        st.warning("If you do not understand some feedback or think there is a mistake, please talk to your tutor. The app can sometimes make small errors.")

        st.markdown("**Learn Language Education Academy** | 🌍 Empowering your German learning journey.")
