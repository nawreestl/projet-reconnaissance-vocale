import streamlit as st
import speech_recognition as sr

# Titre de l'application
st.title('Application de Reconnaissance Vocale')

# Afficher un texte simple
st.write("Appuyez sur le bouton et commencez à parler pour que le texte soit reconnu.")

# Fonction pour capturer la parole
def recognize_speech():
    recognizer = sr.Recognizer()

    # Capture audio du microphone
    with sr.Microphone() as source:
        st.write("Veuillez parler...")
        audio = recognizer.listen(source)
        try:
            # Utiliser le service Google pour la reconnaissance vocale
            text = recognizer.recognize_google(audio, language="fr-FR")
            st.write(f"Vous avez dit: {text}")
        except Exception as e:
            st.write("Désolé, je n'ai pas compris. Essayez encore.")
            st.write(f"Erreur: {e}")

# Ajouter un bouton pour démarrer la reconnaissance vocale
if st.button('Démarrer la reconnaissance vocale'):
    recognize_speech()
