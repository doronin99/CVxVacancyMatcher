import streamlit as st
import requests


def get_compatibility_score(vacancy_description, resume_description):
    api_url = "http://localhost:8000/compatibility"
    payload = {"vacancy_description": vacancy_description, "resume_description": resume_description}
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        return response.json()["compatibility_score"]
    else:
        st.error(f"Error: {response.status_code}")
        return None


def main():
    st.title("Vacancy-Resume Compatibility Checker")

    vacancy_description = st.text_area("Enter Vacancy Description:")
    resume_description = st.text_area("Enter Resume Description:")

    if st.button("Check Compatibility"):
        compatibility_score = get_compatibility_score(vacancy_description, resume_description)
        if compatibility_score is not None:
            st.success(f"Compatibility Score: {compatibility_score}")


if __name__ == "__main__":
    main()
