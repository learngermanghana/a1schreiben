import streamlit as st
import re

st.set_page_config(page_title="A1 Schreiben Trainer", page_icon="✉️")

st.title("✉️ A1 Schreiben Trainer")
st.write("**Learn Language Education Academy** – Letter Writing Practice for A1 Exam")

# ------------------ LETTER TASKS -----------------------

letter_tasks = {
    1: {"task": "Schreiben Sie eine E-Mail an Ihren Arzt und sagen Sie Ihren Termin ab.",
        "points": ["Warum schreiben Sie?", "Sagen Sie: den Grund für die Absage.", "Fragen Sie: nach einem neuen Termin."]},
    2: {"task": "Schreiben Sie eine E-Mail an Ihren Freund und laden Sie ihn zur Feier Ihres neuen Jobs ein.",
        "points": ["Warum schreiben Sie?", "Sagen Sie: wann die Feier ist.", "Fragen Sie: ob er etwas mitbringen kann."]},
    3: {"task": "Schreiben Sie eine E-Mail an einen Freund und teilen Sie ihm mit, dass Sie ihn besuchen möchten.",
        "points": ["Warum schreiben Sie?", "Sagen Sie: wann Sie kommen werden.", "Fragen Sie: was Sie zusammen machen können."]},
    4: {"task": "Schreiben Sie eine E-Mail an eine Kochschule und melden Sie sich für einen Kochkurs an.",
        "points": ["Warum schreiben Sie?", "Fragen Sie: wann der nächste Kurs beginnt.", "Fragen Sie: wie viel der Kurs kostet."]},
    5: {"task": "Schreiben Sie eine E-Mail an eine Sprachschule und fragen Sie nach einem Deutschkurs.",
        "points": ["Warum schreiben Sie?", "Fragen Sie: wann der Kurs beginnt.", "Fragen Sie: wie lange der Kurs dauert."]},
    6: {"task": "Schreiben Sie eine E-Mail an die Bibliothek und fragen Sie, ob Sie ein reserviertes Buch abholen können.",
        "points": ["Warum schreiben Sie?", "Fragen Sie: wann Sie das Buch abholen können.", "Fragen Sie: wie lange Sie es behalten dürfen."]},
    7: {"task": "Schreiben Sie eine E-Mail an einen Freund und laden Sie ihn zu Ihrer Geburtstagsfeier ein.",
        "points": ["Warum schreiben Sie?", "Sagen Sie: wann und wo die Feier stattfindet.", "Fragen Sie: ob er kommen kann."]},
    8: {"task": "Schreiben Sie eine E-Mail an einen Freund und laden Sie ihn zu Ihrer Hochzeit ein.",
        "points": ["Warum schreiben Sie?", "Sagen Sie: wann und wo die Hochzeit ist.", "Fragen Sie: ob er teilnehmen kann."]},
    9: {"task": "Schreiben Sie eine E-Mail an die Touristeninformation und fragen Sie nach Informationen über die Stadt.",
        "points": ["Warum schreiben Sie?", "Fragen Sie: welche Sehenswürdigkeiten es gibt.", "Fragen Sie: nach Hotelvorschlägen."]},
    10: {"task": "Schreiben Sie eine E-Mail an einen Freund und teilen Sie ihm mit, dass Sie in eine neue Wohnung ziehen.",
         "points": ["Warum schreiben Sie?", "Sagen Sie: wann Sie umziehen.", "Fragen Sie: ob er Ihnen beim Umzug helfen kann."]},
    11: {"task": "Schreiben Sie eine E-Mail an Ihren Arzt und fragen Sie nach einem Termin.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: wann der früheste Termin möglich ist.", "Fragen Sie: welche Unterlagen Sie mitbringen sollen."]},
    12: {"task": "Schreiben Sie eine E-Mail an einen Freund und laden Sie ihn ein, Sie in Ihrer Stadt zu besuchen.",
         "points": ["Warum schreiben Sie?", "Sagen Sie: wann er kommen kann.", "Fragen Sie: ob er bei Ihnen übernachten möchte."]},
    13: {"task": "Schreiben Sie eine E-Mail an einen Freund und sagen Sie Ihren geplanten Besuch ab.",
         "points": ["Warum schreiben Sie?", "Entschuldigen Sie sich für die Absage.", "Fragen Sie: ob Sie einen neuen Termin finden können."]},
    14: {"task": "Schreiben Sie eine E-Mail an ein Sportzentrum und fragen Sie nach der Anmeldung für einen Kurs.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: wann der Kurs stattfindet.", "Fragen Sie: welche Kleidung Sie benötigen."]},
    15: {"task": "Schreiben Sie eine E-Mail an ein Geschäft und beschweren Sie sich über ein gekauftes Produkt.",
         "points": ["Warum schreiben Sie?", "Beschreiben Sie das Problem.", "Fragen Sie: nach einer Rückerstattung oder einem Umtausch."]},
    16: {"task": "Schreiben Sie eine E-Mail an einen Freund und gratulieren Sie ihm zu seinem neuen Job.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: wie der neue Job ist.", "Fragen Sie: wann Sie zusammen feiern können."]},
    17: {"task": "Schreiben Sie eine E-Mail an einen Freund und erzählen Sie ihm von Ihren Urlaubsplänen.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: ob er mitkommen möchte.", "Fragen Sie: nach seinen Vorschlägen für Aktivitäten."]},
    18: {"task": "Schreiben Sie eine E-Mail an ein Yogastudio und melden Sie sich für einen Kurs an.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: wann der Kurs beginnt.", "Fragen Sie: wie lange der Kurs dauert."]},
    19: {"task": "Schreiben Sie eine E-Mail an einen Freund und laden Sie ihn zu einem Abendessen bei Ihnen zu Hause ein.",
         "points": ["Warum schreiben Sie?", "Sagen Sie: wann das Abendessen stattfindet.", "Fragen Sie: ob er spezielle Wünsche hat."]},
    20: {"task": "Schreiben Sie eine E-Mail an eine Buchhandlung und fragen Sie, ob sie ein bestimmtes Kochbuch auf Lager haben.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: ob das Buch verfügbar ist.", "Fragen Sie: wie viel es kostet."]},
    21: {"task": "Schreiben Sie eine E-Mail an Frau Müller und reservieren Sie ein Zimmer.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: nach dem Preis für die Nacht.", "Sagen Sie Ihre Ankunftszeit."]},
    22: {"task": "Schreiben Sie eine E-Mail an das Restaurant.",
         "points": ["Warum schreiben Sie?", "Fragen Sie: nach einem Tisch für zwei Personen.", "Sagen Sie: um welche Uhrzeit die Reservierung sein soll."]}
}

# ---------------- LETTER SELECTION -----------------

task_number = st.number_input("Choose a Schreiben task number (1 to 22):", min_value=1, max_value=22)

if task_number in letter_tasks:
    st.markdown(f"### 📄 Aufgabe {task_number}: {letter_tasks[task_number]['task']}")
    st.markdown("**Please include the following points in your letter:**")
    for point in letter_tasks[task_number]['points']:
        st.markdown(f"- {point}")
else:
    st.markdown("Aufgabe für diese Nummer wurde noch nicht definiert.")

# ---------------- LETTER WRITING ------------------

student_letter = st.text_area("✏️ Write your letter here:", height=350)

# ---------------- ANALYSIS -----------------------

def analyze_letter(letter, task_number):
    feedback = []
    score = 25  # Start with full score

    # Greeting
    if not re.search(r"(Sehr geehrte[r]?|Hallo|Lieber|Liebe)", letter):
        feedback.append("❌ Greeting missing or incorrect.")
        score -= 5

    # Closing
    if not re.search(r"(Mit freundlichen Grüßen|Viele Grüße|Liebe Grüße|Dein|Deine)", letter):
        feedback.append("❌ Closing missing or incorrect.")
        score -= 5

    # Conclusion phrase
    if not re.search(r"Ich freue mich im Voraus auf (Ihre|deine) Antwort", letter):
        feedback.append("❌ Conclusion phrase missing or incorrect. Expected phrase: 'Ich freue mich im Voraus auf Ihre/deine Antwort.'")
        score -= 5

    # Connector
    connectors = ["weil", "deshalb", "Ich möchte wissen, ob", "denn", "und", "oder"]
    if not any(conn in letter for conn in connectors):
        feedback.append("❌ No connector found. Try using: 'weil', 'deshalb', 'denn', 'Ich möchte wissen, ob', 'und' or 'oder'.")
        score -= 5

    # Spelling check
    spelling_errors = []
    if re.search(r"\bKostet\b", letter):
        spelling_errors.append("Use lowercase for 'kostet'.")
        score -= 2

    # Declension check
    if re.search(r"eine[rn]? Kochkurs|eine[rn]? Deutschkurs", letter):
        feedback.append("❌ Check your declension: Should be 'einen Kochkurs' or 'einen Deutschkurs'.")
        score -= 3

    # ------------------ Dynamic content check ------------------

    missing_points = []

    # Aufgabe 4: Kochkurs anmelden
    if task_number == 4:
        if not re.search(r"(kochkurs|kurs anmelden|anmeldung)", letter):
            missing_points.append("❌ You did not clearly say why you are writing (registering for a cooking course).")
            score -= 2
        # Improved flexible regex for course start
        if not re.search(r"(wann.*(kurs|koch).*beginn|kursbeginn|wann.*startet|wann.*beginnt|wann.*anfängt)", letter):
            missing_points.append("❌ You did not ask when the course begins.")
            score -= 2
        if not re.search(r"(preis|kosten|wie viel|bezahlen|zahlung)", letter):
            missing_points.append("❌ You did not ask about the course cost or how to pay.")
            score -= 3

    # Aufgabe 12: Einladung an einen Freund
    if task_number == 12:
        if not re.search(r"besuch|besuchen|einladen|möchte dich einladen|laden.*ein", letter):
            missing_points.append("❌ You did not clearly say why you are writing (inviting your friend to visit).")
            score -= 2
        if not re.search(r"(wann|Samstag|Sonntag|Montag|Dienstag|Mittwoch|Donnerstag|Freitag)", letter):
            missing_points.append("❌ You did not say when the friend can come.")
            score -= 2
        if not re.search(r"übernachten|bei mir schlafen|bei mir bleiben", letter):
            missing_points.append("❌ You did not ask if your friend wants to stay overnight.")
            score -= 3

    # You can add more dynamic checks for other tasks later if needed

    if missing_points:
        feedback.extend(missing_points)

    # ------------------ Weil sentence order ------------------

    if "weil" in letter:
        sentences = re.split(r'[.!?]', letter)
        for sentence in sentences:
            if "weil" in sentence:
                weil_part = sentence.split("weil", 1)[-1].strip()
                if not re.search(r'\b\w+(t|en|st|e|te|est|ete|ten|et)\b\s*$', weil_part):
                    feedback.append(f"⚠ Possible word order issue in: '{sentence.strip()}'. The verb should be at the end after 'weil'.")
                    score -= 2

    # ------------------ Formality ------------------

    if re.search(r"Sehr geehrte[r]?|Mit freundlichen Grüßen", letter):
        if "du" in letter:
            feedback.append("⚠️ You mixed formal and informal language. Use either Sie or du consistently.")
            score -= 1

    # ------------------ Spelling summary ------------------

    if spelling_errors:
        feedback.append("🔤 Spelling issues: " + ", ".join(spelling_errors))

    return feedback, max(score, 0)

# ---------------- SUBMIT & FEEDBACK -----------------

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
            for issue in feedback:
                st.write(issue)

        if final_score < 15:
            st.info("Tip: Please review your sentence structure rules or consult your tutor for further guidance.")

        # Extra umlaut spelling tip
        if "mochte" in student_letter and not "möchte" in student_letter:
            st.warning("It looks like you wrote 'mochte' without an umlaut (ö). It should be 'möchte'.")

        # Word count
        word_count = len(student_letter.split())
        st.markdown(f"**Your word count:** {word_count} words")

        st.markdown("---")
        st.markdown("**Learn Language Education Academy** | 🌍 Empowering your German learning journey.")
