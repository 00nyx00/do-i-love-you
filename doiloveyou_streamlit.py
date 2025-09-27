import streamlit as st

st.title("Do I love you?")

# Ask for input via Streamlit
name = st.text_input("Who are you? 🧐").casefold().strip()

love = ["marina", "majdi", "su", "gokcesu", "kira", "mama"]
nope = ["hitler", "pedophile", "carrie bradshaw", "horia brenciu"]

# Only check once input is given
if name:
    if name in love:
        st.success(f"I love you, {name.title()} 🩷")
    elif name == "nyx":
        st.info("Always gotta love myself 💋")
    elif name in nope:
        st.error("Ew. No. Get out of here. 🤢")
    else:
        st.write("You're probably alright I guess. 👍")
