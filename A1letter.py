# ===== Stage 1: Imports, Configuration & UI Setup =====
import streamlit as st
import re
import random

st.set_page_config(page_title="A1 Schreiben Trainer", page_icon="✉️")

st.title("✉️ A1 Schreiben Trainer")
st.write("**Learn Language Education Academy** – Letter Writing Practice for A1 Exam")

# Student login and pledge
student_name = st.text_input("Please enter your name:")
pledge = st.checkbox("✅ I promise to write my own letter and not overuse translators.")

if not student_name or not pledge:
    st.warning("Please enter your name and accept the pledge before continuing.")
    st.stop()

st.success(f"Welcome, {student_name}! You may now begin.")

# Load tasks
tasks = {
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
         "points": ["Glückwunsch zum Job.", "Fragen Sie, wie der neuen Job ist.", "Vorschlag: gemeinsam feiern."]},
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

# Task selection with plus/minus buttons
task_number = st.number_input(
    f"Choose a Schreiben task number (1 to {len(tasks)})",
    min_value=1,
    max_value=len(tasks),
    value=1,
    step=1
)

if task_number in tasks:
    st.markdown(f"### 📄 Aufgabe {task_number}: {tasks[task_number]['task']}")
    st.markdown("**Include the following points:**")
    for p in tasks[task_number]['points']:
        st.markdown(f"- {p}")

student_letter = st.text_area("✏️ Write your letter here:", height=350)

# ===== Stage 2: Analysis Logic & Submission =====

WORD_MOCHTE = re.compile(r"\bmochte\b", re.IGNORECASE)
modal_verbs = ["möchte", "möchten", "kann", "können", "kannst", "will", "wollen"]


def analyze_letter(letter, task_number):
    feedback = []
    score = 25

    letter = WORD_MOCHTE.sub("möchte", letter)
    sentences = re.split(r'(?<=[.!?])\s+', letter.strip())

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        words = re.findall(r"\w+", sent)

        # Skip checks for 'Ich möchte wissen' or 'denn ich möchte'
        if sent.lower().startswith("ich möchte wissen") or sent.lower().startswith("denn ich möchte"):
            continue

        # Error checks for article with *kurs (Akkusativ masculines)
        lower_sent = sent.lower()
        for course in ["kochkurs", "deutschkurs", "sprachkurs"]:
            if re.search(rf"\beine\s+{course}\b", lower_sent):
                course_cap = course.capitalize()
                feedback.append(f"⚠ '{course_cap}' is masculine. Use 'einen {course_cap}' (Akkusativ).")
                score -= 2
        # Spelling corrections
        if "kockkurs" in lower_sent:
            feedback.append("🔤 Spelling mistake: 'Kockkurs' should be 'Kochkurs'.")
            score -= 1
        # Mid-sentence 'Kostet' check
        words_sent = re.findall(r"\w+", sent)
        for w in words_sent[1:]:
            if w == "Kostet":
                feedback.append("⚠ 'kostet' should not be capitalized mid-sentence.")
                score -= 1
                break

        # Find first modal verb index
        modal_idx = None
        for i, w in enumerate(words):
            if w.lower() in modal_verbs:
                modal_idx = i
                break

        if modal_idx is not None:
            if 'weil ich' in sent.lower():
                # Modal verb must be last word
                if words[-1].lower() not in modal_verbs:
                    feedback.append(f"⚠ After 'weil ich', the modal verb should be the last word: '{sent}'")
                    score -= 1
            elif 'weil ' in sent.lower():
                # Other 'weil' sentences allow 'e' or 'en'
                last = words[-1].lower()
                if not (last.endswith('e') or last.endswith('en')):
                    feedback.append(f"⚠ Sentence should end with 'e' or 'en' after 'weil': '{sent}'")
                    score -= 1
            else:
                # Modal position
                if modal_idx > 1:
                    feedback.append(f"⚠ Modal verb appears at position {modal_idx+1} in sentence: '{sent}'")
                    score -= 1
                # Infinitive ending for non-weil sentences when modal at pos0/1
                if modal_idx <= 1:
                    last = words[-1].lower()
                    if not last.endswith('en'):
                        feedback.append(f"⚠ Sentence should end with an infinitive verb (ending in 'en'): '{sent}'")
                        score -= 1

    # Points coverage
    missing = []
    for point in tasks[task_number]['points']:
        if point.strip().lower() == "warum schreiben sie?":
            if re.search(r"\bich schreibe (ihnen|dir)\b", letter.lower()):
                continue
        kws = [w for w in re.findall(r"\w+", point.lower()) if w not in ['sie','den','der','das']]
        if not any(k in letter.lower() for k in kws):
            missing.append(point)
    if missing:
        feedback.append("⚠ Missing required points:")
        feedback.extend([f"- {mp}" for mp in missing])
        score -= 3

    return feedback, max(score, 0)

# Submission handling
if st.button("✅ Submit Letter"):
    if len(student_letter.strip()) < 20:
        st.warning("Write a longer letter before submitting.")
    else:
        feedback, score = analyze_letter(student_letter, task_number)
        st.subheader("📝 Feedback & Score")
        st.write(f"Score: {score}/25")
        for f in feedback:
            st.markdown(f"- {f}")
        wc = len(re.findall(r"\w+", student_letter))
        st.markdown(f"**Word count:** {wc}")
