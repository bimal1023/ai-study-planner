import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

if "study_plan" not in st.session_state:
    st.session_state.study_plan = ""

st.title("AI Study Planner")
st.write("An AI-powered study planner that generates personalized schedules based on your exams and weak topics.")
st.write("Enter your study details and get a simple study plan.")

subjects = st.text_area(
    "Enter your subjects and exam dates",
    placeholder="Example:\nMath - April 20\nComputer Science - April 15\nHistory - April 25"
)

hours_per_day = st.number_input(
    "How many hours can you study per day?",
    min_value=1,
    max_value=8,
    value=3
)

weak_topics = st.text_area(
    "Enter weak topics",
    placeholder="Example:\nRecursion\nIntegration\nDatabase joins"
)

days_to_plan = st.number_input(
    "How many days do you want in the plan?",
    min_value=1,
    max_value=30,
    value=7
)

if st.button("Generate Study Plan"):
    if subjects.strip():
        prompt = f"""
You are a helpful academic study planner.

Create a realistic {days_to_plan}-day study plan for a student.

Student subjects and exam dates:
{subjects}

Weak topics:
{weak_topics}

Available study hours per day:
{hours_per_day}

Instructions:
- Prioritize subjects with earlier exam dates
- Give extra focus to weak topics
- Do not exceed the available study hours per day
- Make the plan beginner-friendly and realistic
- Balance subjects across days
- Avoid overloading a single day
- Mix difficult and easy topics

Output:
1. Priority order of subjects
2. A day-by-day study plan
3. 3 short study tips
"""

        with st.spinner("Generating your study plan... ⏳"):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You create simple, realistic study plans for students."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content
            st.session_state.study_plan = result
    else:
        st.warning("Please enter your subjects and exam dates.")

if st.session_state.study_plan:
    st.subheader("Your Study Plan")
    st.markdown(st.session_state.study_plan)

    st.download_button(
        label="Download Study Plan",
        data=st.session_state.study_plan,
        file_name="study_plan.txt",
        mime="text/plain"
    )

    st.subheader("Ask about your study plan")
    user_question = st.text_input("Ask a follow-up question about your plan")

    if st.button("Ask AI About My Plan"):
        if user_question.strip():
            followup_prompt = f"""
You are a study planning assistant.

Here is the student's current study plan:
{st.session_state.study_plan}

User question:
{user_question}

Give a helpful, clear answer based on the plan above.
"""

            with st.spinner("Thinking... 🤔"):
                followup_response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "You help students understand and adjust their study plans."},
                        {"role": "user", "content": followup_prompt}
                    ]
                )

                followup_result = followup_response.choices[0].message.content
                st.subheader("AI Response")
                st.markdown(followup_result)
        else:
            st.warning("Please enter a question.")