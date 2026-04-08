# AI Study Planner

An AI-powered study planner built with **Python**, **Streamlit**, and the **OpenAI API**.  
It generates personalized study schedules based on exam dates, weak topics, and available study time.

## Features

- Generate AI-based study plans
- Prioritize subjects by exam dates
- Focus on weak topics
- Ask follow-up questions about the plan
- Download study plan
- Clean UI with loading indicators

## Tech Stack

- Python
- Streamlit
- OpenAI API
- python-dotenv

## Installation

```bash
git clone https://github.com/bimal1023/ai-study-planner.git
cd ai-study-planner

conda create -n study-planner python=3.11
conda activate study-planner

pip install -r requirements.txt
```
## Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```
## Run
```
streamlit run app.py
```
