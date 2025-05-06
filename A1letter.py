import streamlit as st
import re
import random

st.set_page_config(page_title="A1 Schreiben Trainer", page_icon="✉️")

st.title("✉️ A1 Schreiben Trainer")
st.write("**Learn Language Education Academy** – Letter Writing Practice for A1 Exam")

# ------------------ LETTER TASKS -----------------------

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

# ---------------- LETTER SELECTION -----------------

task_number = st.number_input(
    "Choose a Schreiben task number (1 to 22):",
    min_value=1,
    max_value=22,
    key="task_number_input"
)

if task_number in letter_tasks:
    st.markdown(f"### 📄 Aufgabe {task_number}: {letter_tasks[task_number]['task']}")
    st.markdown("**Please include the following points in your letter:**")
    for point in letter_tasks[task_number]['points']:
        st.markdown(f"- {point}")
else:
    st.markdown("Aufgabe für diese Nummer wurde noch nicht definiert.")

# ------------------ CHEAT SHEET ------------------

with st.expander("📝 Show A1 Schreiben Cheat Sheet"):
    st.markdown("### Polite Requests")
    st.markdown("- Ich möchte ...")
    st.markdown("- Können Sie bitte ...")
    st.markdown("- Könnten Sie mir ... mitteilen?")
    st.markdown("- Ich brauche ...")

    st.markdown("### Asking for Information")
    st.markdown("- Ich möchte wissen, ob ...")
    st.markdown("- Ich möchte wissen, wann ...")

    st.markdown("### Giving Reasons")
    st.markdown("- weil ...")
    st.markdown("- denn ...")
    st.markdown("- deshalb ...")

    st.markdown("### Apologies")
    st.markdown("- Es tut mir leid.")
    st.markdown("- Ich entschuldige mich ...")

    st.markdown("### Asking Questions")
    st.markdown("- Wie viel ...")
    st.markdown("- Wann ...")

    st.markdown("### Greetings")
    st.markdown("- Hallo")
    st.markdown("- Sehr geehrte/r ... (formal)")
    st.markdown("- Lieber/Liebe ... (informal)")

    st.markdown("### Closings")
    st.markdown("- Mit freundlichen Grüßen")
    st.markdown("- Viele Grüße")
    st.markdown("- Liebe Grüße")

    st.markdown("### Conclusion Phrase")
    st.markdown("- Ich freue mich im Voraus auf Ihre/deine Antwort.")

# ---------------- LETTER WRITING ------------------

student_letter = st.text_area("✏️ Write your letter here:", height=350)

def analyze_letter(letter, task_number):
    feedback = []
    score = 25

    # -------- GREETING CHECK --------
    if not re.search(r"(Sehr geehrte[r]?|Hallo|Lieber|Liebe)", letter):
        feedback.append("❌ Greeting missing or incorrect.")
        score -= 5

    # -------- CLOSING CHECK --------
    if not re.search(r"(Mit freundlichen Grüßen|Viele Grüße|Liebe Grüße|Dein|Deine)", letter):
        feedback.append("❌ Closing missing or incorrect.")
        score -= 5

    # -------- FORMALITY DETECTION --------
    formal = bool(re.search(r"(Sehr geehrte[r]?|Mit freundlichen Grüßen)", letter))
    informal = bool(re.search(r"(Hallo|Lieber|Liebe|Viele Grüße|Liebe Grüße|Dein|Deine)", letter))

    # -------- CONCLUSION PHRASE CHECK WITH FORMALITY --------
    conclusion_match = re.search(
        r"ich\s+freue\s+mich\s+im\s+voraus\s+auf\s+(ihre|deine|eure)\s+antwort",
        letter, re.IGNORECASE
    )

    if conclusion_match:
        used_form = conclusion_match.group(1).lower()

        if formal and used_form != "ihre":
            feedback.append("⚠ You used 'deine Antwort' but the letter is formal. Use 'Ihre Antwort'.")
            score -= 3
        elif informal and used_form == "ihre":
            feedback.append("⚠ You used 'Ihre Antwort' but the letter seems informal. You can write 'deine Antwort'.")
            score -= 1
    else:
        student_version = re.findall(r"freue.*antwort.*", letter, re.IGNORECASE)
        if student_version:
            feedback.append(
                f"❌ Conclusion phrase incorrect. Your version: '{student_version[0]}'. Expected: 'Ich freue mich im Voraus auf Ihre/deine Antwort.'"
            )
        else:
            feedback.append("❌ Conclusion phrase missing.")
        score -= 5

    # -------- CONNECTOR CHECK --------
    connectors = ["weil", "denn", "deshalb", "ich möchte wissen, ob", "ich möchte wissen, wann"]
    if not any(conn in letter.lower() for conn in connectors):
        feedback.append("❌ No connector found. Use 'weil', 'denn', 'deshalb' or 'ich möchte wissen, ob/wann'.")
        score -= 5

    # -------- A1 PHRASES CHECK --------
    a1_phrases = [
        "ich möchte", "können sie bitte", "könnten sie mir", "ich brauche",
        "ich möchte wissen, ob", "ich möchte wissen, wann",
        "weil", "denn", "deshalb",
        "es tut mir leid", "ich entschuldige mich",
        "wie viel", "wann"
    ]
    if not any(phrase in letter.lower() for phrase in a1_phrases):
        feedback.append("⚠ Important A1 phrases missing (e.g., 'ich möchte' or 'könnten Sie mir').")
        score -= 3

    # -------- SPELLING/CAPITALIZATION CHECK (fixed "Ich" issue) --------
    if re.search(r"\bich\b", letter) and not re.search(r"\bIch\b", letter):
        feedback.append("🔤 'Ich' should always be capitalized.")
        score -= 1

    if re.search(r"\bKostet\b", letter):
        feedback.append("🔤 'kostet' should not be capitalized.")
        score -= 2

    common_words = ["möchte", "möglich"]
    for word in common_words:
        if re.search(rf"\b{word.capitalize()}\b", letter):
            feedback.append(f"🔤 Capitalization error: '{word}' should not be capitalized.")
            score -= 1

    # -------- DECLENSION CHECK --------
    if re.search(r"eine[rn]? Kochkurs|eine[rn]? Deutschkurs", letter):
        feedback.append("❌ Declension error: Should be 'einen Kochkurs' or 'einen Deutschkurs'.")
        score -= 3

    # -------- 'WEIL' SENTENCE ORDER CHECK --------
    if "weil" in letter.lower():
        sentences = re.split(r'[.!?]', letter)
        for sentence in sentences:
            if "weil" in sentence:
                weil_part = sentence.split("weil", 1)[-1].strip()
                if not re.search(r'\b\w+(t|en|st|e|te|est|ete|ten|et)\b', weil_part):
                    feedback.append(f"⚠ Possible word order issue after 'weil' in: '{sentence.strip()}'.")
                    score -= 2

    # -------- PUNCTUATION CHECK --------
    if not re.search(r'[.!?]', letter):
        feedback.append("⚠ No sentence-ending punctuation found. Remember to end sentences with a full stop or question mark.")
        score -= 2

    # -------- WRONG QUESTION MARK AFTER "Ich hoffe..." --------
    wrong_question = re.findall(r"ich hoffe[^.?!]*\?", letter, re.IGNORECASE)
    if wrong_question:
        feedback.append("⚠ You wrote a sentence like 'Ich hoffe ... ?' but it should end with a full stop, not a question mark.")
        score -= 1

    # -------- FORMALITY CONSISTENCY CHECK --------
    if formal and re.search(r"\bdu\b", letter):
        feedback.append("⚠ You mixed formal and informal language. Use either Sie or du consistently.")
        score -= 1

    # -------- QUESTION FORM CHECK --------
    question_found = False
    sentences = re.split(r'[.!?]', letter)

    for sentence in sentences:
        sentence_clean = sentence.strip()
        if "?" in sentence or re.search(r"(ist|sind|kann|können|haben|hat|wann|wie|wer|was|wo|warum|möchte)", sentence_clean, re.IGNORECASE):
            question_found = True
            if re.search(r'\?$', sentence):
                if not re.match(
                    r"^\s*(ist|sind|kann|können|haben|hat|wann|wie|wer|was|wo|warum|möchte|konnen)",
                    sentence_clean, re.IGNORECASE):
                    feedback.append(
                        f"⚠ This might not be a correct question form in: '{sentence_clean}'."
                    )
                    score -= 2

    if not question_found:
        feedback.append("⚠ No questions found. Remember to include a question.")
        score -= 2

    # -------- TOPIC KEYWORDS CHECK --------
    topic_keywords = {
        1: ["arzt", "termin", "absagen", "verschieben", "schmerzen"],
        2: ["feier", "feiern", "job", "einladen"],
        3: ["besuch", "besuchen", "einladen"],
        4: ["koch", "kurs", "anmeldung"],
        5: ["deutschkurs", "sprachkurs", "lernen", "anmeldung"],
        6: ["buch", "bibliothek", "abholen"],
        7: ["geburtstag", "party", "einladen"],
        8: ["petra", "besuch", "absagen", "verschieben"],
        9: ["wohnung", "apartment", "mieten", "haussuche"],
        10: ["berlin", "hotel", "sehenswürdigkeiten", "buchen", "bezahlen"],
        11: ["arzt", "termin", "fragen", "schmerzen"],
        12: ["besuch", "einladen", "übernachten"],
        13: ["absagen", "verschieben", "entschuldigen"],
        14: ["schule", "sohn", "entschuldigung", "krank", "schmerzen"],
        15: ["produkt", "problem", "reklamieren", "rückgabe"],
        16: ["party", "besprechung", "spät", "hilfe"],
        17: ["gratulieren", "job", "feiern"],
        18: ["sachsen", "hotel", "sehenswürdigkeiten", "buchen", "bezahlen"],
        19: ["yogakurs", "kurs", "anmeldung"],
        20: ["krank", "absagen", "termin", "schmerzen"],
        21: ["zimmer", "hotel", "reservieren", "buchen", "bezahlen"],
        22: ["restaurant", "tisch", "reservieren"],
    }

    keywords = topic_keywords.get(task_number, [])
    if keywords:
        if not any(word in letter.lower() for word in keywords):
            feedback.append("⚠ Your letter content might not match the selected task.")
            score -= 2

    # -------- TASK POINTS CHECK (IMPROVED) --------
    missing_points = []
    for point in letter_tasks[task_number]['points']:
        point_keywords = [word for word in re.findall(r'\w+', point.lower())
                          if word not in ["sie", "den", "der", "das", "die", "warum", "wann", "wie", "was", "ob", "und", "oder", "mit"]]

        found = False
        for keyword in point_keywords:
            for student_word in re.findall(r'\w+', letter.lower()):
                matches = sum(1 for c in keyword if c in student_word)
                if matches >= len(keyword) * 0.7:
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

    return feedback, max(score, 0)

# ---------------- SUBMIT BUTTON & FEEDBACK ------------------

if st.button("✅ Submit Letter", key="submit_button"):
    if len(student_letter.strip()) < 20:
        st.warning("Please write a longer letter before submitting.")
    else:
        feedback, final_score = analyze_letter(student_letter, task_number)

        st.subheader("📝 Analysis & Feedback")

        if final_score == 25:
            st.success("✅ Excellent! Your letter meets all the important requirements.")
        else:
            st.error(f"Your score: {final_score}/25")
            st.markdown("### Feedback:")
            for item in feedback:
                st.markdown(f"- {item}")

        # -------- Word count & Tip --------
        word_count = len(student_letter.split())
        st.markdown(f"**Your word count:** {word_count} words.")

        if word_count < 40:
            st.info("✏️ Your letter is a bit short. Aim for at least 40–60 words for A1 writing tasks.")

        # -------- Möchte / mochte Check --------
        if "mochte" in student_letter and not "möchte" in student_letter:
            st.warning("It looks like you wrote 'mochte' without an umlaut (ö). On most keyboards, press and hold 'o' to see 'ö'.")

        st.markdown("---")

        # ------------------ MOTIVATIONAL TIPS ------------------

        tips = [
            "🔎 Tip: Don’t forget to always write 'möchte' with the umlaut (ö).",
            "💡 Tip: Yes/No questions should start with the verb. Example: 'Ist...', 'Haben...', 'Können...'.",
            "📝 Tip: Remember to end your letter with 'Mit freundlichen Grüßen'.",
            "📝 Tip: Use 'weil' or 'denn' to explain reasons.",
            "🔤 Tip: 'kostet' should not be capitalized unless at the beginning of a sentence.",
            "💬 Tip: For questions, start with 'Ist', 'Haben', 'Können' or 'Wann'.",
            "🌟 Tip: Practice writing short emails every day to improve sentence structure.",
            "📌 Tip: Use 'Ich möchte wissen, ob...' for polite indirect questions.",
            "✅ Tip: Always include a reason for writing, a question, and a closing phrase."
        ]

        st.info(random.choice(tips))

        st.markdown("---")

        # -------- Tutor reminder --------
        st.warning("If you do not understand some feedback or think there is a mistake, please talk to your tutor. "
                   "The app can sometimes make small errors.")

        st.markdown("**Learn Language Education Academy** | 🌍 Empowering your German learning journey.")
