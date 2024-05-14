import streamlit as st
from groq import Groq
import json

# Get the API key from Streamlit secrets
groq_api_key = st.secrets["GROQ_API_KEY"]

# Set up API key and initialize Groq client
groq_client = Groq(api_key=groq_api_key)

# Main system message for MySpaceFactor with property details
main_system_message = """
You are an assistant for MySpaceFactor, a real estate firm dedicated to helping clients find their perfect homes. Provide insightful, professional, and helpful responses.
Company: MySpaceFactor

### Properties:

1. **Garudadri Gardens Apartment**:
   - Location: RR Nagar (Kengeri), next to P M Santhosh hospital
   - 56 flats, 14 flats each floor, Ground+3 structure
   - No common wall for all units
   - 2BHK and 3BHK available
   - Dimensions: 
     - 2BHK: 1065 to 1200 sqft
     - 3BHK: 1375 to 1500 sqft
   - Amenities: Children's play area, Gym, 6 feet jogging track, Sitting area, Flowers and Herbal gardens, Swimming pool, Party hall

2. **Vasudha Parkone Apartment**:
   - Location: Behind Road of Prestige Lake Ridge, Subramanyapura Road, Uttarahalli, South Bangalore
   - 92 flats, Slit + Ground + 3 structure
   - 2BHK and 3BHK available
   - Dimensions:
     - 2BHK: 1176 to 1213 sqft
     - 3BHK: 1280 to 1343 sqft
   - Offer Price: 5,700 per sqft + additional charges, GST, and Registration.
   - Amenities: 20+ amenities including a children's play area, gym, swimming pool, and more.

3. **Ahaa by Suraksha Group**:
   - Location: Begur Koppa Road, 10 mins from Meenakshi Mall
   - Boutique community with amenities for everyone in the family
   - Possession: Jan 2024
   - Prices starting at 85 Lakh* with an exciting launch offer.

4. **Suraksha Heritage Park**:
   - Location: Off Bannergatta Road (Begur Road), 10 mins from Hulimavu Metro station
   - 2.27 Acre, 198 Units, 3 towers, B+G+11
   - 2BHK: 1134 sqft - 82 Lakh
   - 3BHK: 1600 sqft - 1.08 Cr
   - 3BHK: 1672 sqft - 1.19 Cr
   - 30+ amenities, no common walls, 100% vaastu

5. **Budigere by Godrej Properties**:
   - Well connected to Whitefield and Hoskote industrial area
   - Forest Theme based project
   - 3B+G+39, 28 acres
   - Launching: 13 towers with 2000 units
   - Typology:
     - 2BHK: 1285 sqft
     - 3BHK Premium: 1700 sqft (2T)
     - 3BHK Luxe: 2025 sqft (3T)
     - 3.5BHK: 2435-2473 sqft
     - 4.5BHK: 2898 sqft

6. **Elegant Hermitage**:
   - Location: Banashankari 6th stage
   - 2.46 acres, 3 towers, 2B+12 floors
   - 2BHK: 1206-1332 sqft
   - 3BHK: 1548-1719 sqft
   - 4BHK: 2381 sqft
   - Prices: 2BHK from 90 Lakh, 3BHK from 1.15 Cr, 4BHK from 1.9 Cr

7. **RajSri by Vishnu Sri Builders**:
   - Location: 1km from Mysore Road, Rajarajeshwari Nagar Metro Station
   - 2.5 acres, 2 towers, G+9
   - 2BHK: 973-1123 sqft
   - 3BHK: 1399-1476 sqft
   - Possession: Sep 2024

8. **TG Developers - Abode**:
   - Location: Vijaya Bank Layout, Bannerghatta Road
   - Plot Dimensions: 30x40, 30x50
   - Ready to Move
   - Offer Price: 9000 per sqft

9. **SDMV Elite**:
   - Location: Electronic City Phase 2
   - 168 flats, BMRDA approved
   - 2BHK: 880-1200 sqft, Price: 51-65 Lakh
   - 3BHK: 1280-1425 sqft, Price: 75-83.5 Lakh
   - Possession: Block A (Dec 2023), Blocks B & C (Dec 2024)

10. **Pioneer KRS Park Royal Wing-2**:
    - Location: Near RV College, Pattanagere Metro Station
    - 5 acres, 72% open space
    - 2BHK: 1200+ to 1300+ sqft
    - 3BHK: 1400+ to 1800+ sqft
    - Possession: June 2026

11. **Esteem South Park**:
    - Location: Bannerghatta Main Road, Gottigere
    - Premium development, 2BHK and 2.5BHK units
    - Phase 1 and Phase 2 under construction
    - Amenities: Rooftop Party Hall, Gymnasium, Pets Park, Squash court, and more.

12. **Bay Vista by SNN Raj Corp**:
    - Location: Off Banerghatta Road, Behind Indian Institute of Management (IIM) – Bangalore
    - 4.8 acres, G+15 floors
    - 2BHK: 1235-1320 sqft, Price: 1.1-1.35 Cr
    - 3BHK: 1530-1890 sqft, Price: 1.5-2 Cr
    - 4BHK: 2330 sqft, Price: 2.2-2.5 Cr

13. **Saiven Mulberry Groves**:
    - Limited edition lifestyle villas, 6 acres, 75 villas
    - Approved by BMRDA
    - Possession: Dec 2025
    - Villa built-up area: 3028 & 3407 sqft
    - Villa land area: 2250 & 2350 sqft

14. **Ceasar Palace**:
    - Location: Kanakapura Rd, Bangalore City Municipal Corporation Layout
    - 4.98 acres, 498 units, G+17 floors
    - 2BHK and 3BHK luxurious flats
    - Ready to move in
    - Amenities: 25000 sqft club house, luxury indoor and outdoor activities

15. **HM Indigo**:
    - Location: 9th phase JP Nagar
    - Ready to move in
    - 2BHK: 1331 sqft, Price: 1-1.16 Cr
    - 3BHK: 1719 sqft, Price: 1.3-1.4 Cr

16. **MGR Windsor Gardens**:
    - Location: JP Nagar 5th phase
    - Possession: July 2024
    - 2BHK: 1210-1310 sqft
    - 3BHK: 1530-1720 sqft
    - Total units: 36
    - Available units: 14
    - Amenities: Party hall, Gym, Children's play area, CCTV, Power backup, Lift

17. **Sonin Park South**:
    - Location: JP Nagar 8th phase, Near Skalvi International School
    - 2 blocks, G+3 floors, Total units: 32
    - Amenities: Swimming pool, Power backup, Vehicle charger, Children's play area, Gym, Party hall, 24 hrs security

For more information, please contact us at: 9708045117.
"""

# Individual assistant prompts
assistants = {
    "Raghav": {
        "description": "Raghav is eccentric.",
        "prompt": "You are Raghav, an eccentric assistant with unique perspectives. Be witty, creative, and slightly unconventional."
    },
    "Pranav": {
        "description": "Pranav is calm and sweet.",
        "prompt": "You are Pranav, a calm and sweet assistant. Be kind, patient, and supportive."
    },
    "Monesh": {
        "description": "Monesh is cocky.",
        "prompt": "You are Monesh, a cocky assistant. Be confident, assertive, and slightly arrogant."
    }
}

# Initialize chat history and selected assistant in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_assistant" not in st.session_state:
    st.session_state.selected_assistant = "Raghav"

# Main UI
st.set_page_config(page_title="MySpaceFactor", layout="wide")

st.title("MySpaceFactor")
st.write("Helping you find your perfect home. Talk to our virtual assistant for any inquiries.")

# Dropdown for assistant selection
assistant_choice = st.selectbox("Choose your assistant:", list(assistants.keys()))

# Update selected assistant in session state
if st.session_state.selected_assistant != assistant_choice:
    st.session_state.selected_assistant = assistant_choice
    st.session_state.chat_history = []  # Clear chat history on assistant change

# Combine main system message with selected assistant's prompt
system_message = f"{main_system_message}\n{assistants[st.session_state.selected_assistant]['prompt']}"

# Add the system message to chat history if it's empty
if not st.session_state.chat_history:
    st.session_state.chat_history.append({"role": "system", "content": system_message})

# Display selected assistant's description
st.write(f"**Current Assistant: {st.session_state.selected_assistant}**")
st.write(assistants[st.session_state.selected_assistant]['description'])

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(
            f"<div style='border: 2px solid blue; padding: 10px; margin: 10px 0; border-radius: 8px; width: 80%; float: right; clear: both;'>{message['content']}</div>",
            unsafe_allow_html=True
        )
    elif message["role"] == "assistant":
        st.markdown(
            f"<div style='border: 2px solid orange; padding: 10px; margin: 10px 0; border-radius: 8px; width: 80%; float: left; clear: both;'>{message['content']}</div>",
            unsafe_allow_html=True
        )

# Function to handle sending a message
def send_message():
    if st.session_state.input_buffer:
        message = st.session_state.input_buffer  # Store the input in a variable

        # Append user input to chat history
        st.session_state.chat_history.append({"role": "user", "content": message})

        # Call Groq API with the entire chat history
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.chat_history,
            temperature=0.3,
            max_tokens=2000
        )
        chatbot_response = response.choices[0].message.content.strip()

        # Append chatbot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": chatbot_response})

        # Clear the input buffer and trigger rerun
        st.session_state.input_buffer = ""
        st.session_state.run_count += 1  # Trigger a rerun by updating session state

if "run_count" not in st.session_state:
    st.session_state.run_count = 0  # Initialize run count

user_input = st.text_input("Type your message here:", key="input_buffer")
st.button("Send", on_click=send_message)

# Dummy element to force rerun without showing error
st.write(f"Run count: {st.session_state.run_count}")
