import streamlit as st
import requests


def get_cv(vacancy_description):
    api_url = "http://localhost:8080/get_resumes"
    payload = {"text": vacancy_description}
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        return response.text
    else:
        st.error(f"Error: {response.status_code}")
        return None
    

def get_vaccancy(resume_description):
    api_url = "http://localhost:8080/get_vaccancies"
    payload = {"text": resume_description}
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        return response.text
    else:
        st.error(f"Error: {response.status_code}")
        return None


def main():
    st.title("Подбор вакансий/резюме")

    cv_or_vac = st.sidebar.selectbox('Что вы ищите', ('Резюме', 'Вакансия'))

    if cv_or_vac == "Резюме":
        vacancy_description = st.text_area("Введите вашу вакансию:")
        if st.button("Подобрать резюме"):
            result = get_cv(vacancy_description)
            if result is not None:
                st.text(result)
    elif cv_or_vac == "Вакансия":
        resume_description = st.text_area("Введите ваше резюме:")
        if st.button("Подобрать вакансию"):
            result = get_vaccancy(resume_description)
            if result is not None:
                st.text(result)
    else:
        st.text("Выберите, что вы ищите")


if __name__ == "__main__":
    main()
