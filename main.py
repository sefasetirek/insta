import streamlit as st
from utils import generate_content
import json
import datetime

st.set_page_config(page_title="Instagram İçerik Planlayıcı", layout="wide")

st.title("📅 30 Günlük Instagram İçerik Planlayıcı")

with st.form("user_input"):
    col1, col2 = st.columns(2)
    with col1:
        account_name = st.text_input("Instagram Hesap Adı")
        industry = st.selectbox("Sektör", ["Moda", "Teknoloji", "Yiyecek", "Seyahat", "Eğitim", "Diğer"])
        language = st.selectbox("Dil", ["Türkçe", "English", "Deutsch", "Français", "Italiano", "Español", "Ελληνικά", "Русский"])
    with col2:
        target_country = st.text_input("Hedef Ülke")
        target_audience = st.text_area("Hedef Kitle", help="Örn: Gençler, anneler, sporcular...")
        goal = st.text_area("Hesabın Amacı", help="Örn: Ürün satışı, marka bilinirliği...")

    submitted = st.form_submit_button("Plan Oluştur")

if submitted:
    st.info("Plan oluşturuluyor, lütfen bekleyin...")

    with open("plan_templates/prompt_template.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    try:
        with open("data/holidays.json", "r", encoding="utf-8") as f:
            holidays_data = json.load(f)
            country_holidays = holidays_data.get(target_country.lower(), [])
            today = datetime.date.today()
            upcoming_holidays = [h for h in country_holidays if datetime.date.fromisoformat(h["date"]) >= today]
    except:
        upcoming_holidays = []

    prompt = prompt_template.format(
        account_name=account_name,
        industry=industry,
        language=language,
        target_country=target_country,
        target_audience=target_audience,
        goal=goal,
        holidays=",".join([h["name"] for h in upcoming_holidays[:5]])
    )

    plan = generate_content(prompt)

    st.success("İçerik planı oluşturuldu!")
    st.text_area("📆 30 Günlük İçerik Planı", plan, height=500)
