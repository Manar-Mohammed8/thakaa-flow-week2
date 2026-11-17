import streamlit as st
import pandas as pd

st.set_page_config(page_title="Space Scale")

GRAVITY = {"Mercury": 0.38, "Venus": 0.90, "Earth": 1.00, "Moon": 0.17, "Mars": 0.38,
           "Jupiter": 2.53, "Saturn": 1.07, "Uranus": 0.89, "Neptune": 1.14}

st.title("Space Scale")
st.write("اعرفي كم يكون وزنك على الكواكب الأخرى.")

weight = st.number_input("Your weight on Earth (kg)", min_value=1.0, max_value=300.0, value=60.0, step=1.0)
planet = st.selectbox("Choose a world", list(GRAVITY.keys()))

g = GRAVITY[planet]
new_weight = weight * g
st.metric(f"Your weight on {planet}", f"{new_weight:.1f} kg", delta=f"{new_weight - weight:.1f} kg vs Earth")

if g < 1:
    st.success(f"You could jump {1 / g:.1f} times higher on {planet}!")
elif g > 1:
    st.warning(f"You would feel {g:.2f} times heavier on {planet}.")
else:
    st.info("This is Earth, nothing changes.")

st.subheader("Your weight on all worlds")
df = pd.DataFrame({"World": list(GRAVITY.keys()),
                   "Weight (kg)": [weight * v for v in GRAVITY.values()]}).set_index("World")
st.bar_chart(df)