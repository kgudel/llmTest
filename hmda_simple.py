import google.generativeai as genai

genai.configure(api_key="AIzaSyDvm61pIbDxNanP0ceoEO9FE-5Z2UF90m0")

question = "What is a horse"

prompt = "Which of the passages from the following list best matches this question:"  + question + "When answering only respond with the list index of the passage you have selected."

options = [
    "Snapshot Dataset​ \nThe Snapshot dataset is taken at a fixed date after the timely filing deadline has passed, typically one month after March 1. In the event that the dataset is regenerated after publication of the Snapshot, the published date for this dataset will be updated to reflect the new date.",
    "One Year Dataset​ \nThe One Year dataset is taken at least 12 months after the timely filing deadline has passed for a given filing year and incorporates any resubmissions or late submissions that have been completed in that timeframe.\nPlease note that due to the timing of the One Year data product's creation:\nThe 2019 One Year datasets contain more than 12 months worth of updates.\nThere are no One Year datasets for 2017 or 2018.",
    "Three Year Dataset​\nThe Three Year dataset is taken at least 34 months after the timely filing deadline has passed for a given filing year and incorporates any resubmissions or late submissions that have been completed in that timeframe. The Three Year dataset is the final dataset published for any given collection year."
]

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(prompt + " " + str(options)).text.strip()

if response.isdigit():
    integer = int(response)
    print(options[integer])  # Output: 42
else:
    print("IT DIDN'T WORK!!!!")
print(response)