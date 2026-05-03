import streamlit as st
import requests

st.set_page_config(page_title="Decision Helper", layout="centered")

st.title("🧠 Help Me Decide")

# --- Input section ---
st.subheader("Your situation")


user_input = ""


user_input = st.text_area("Describe your situation:", height=150)



# --- Action button ---
if st.button("🚀 Help Me Decide"):

    if not user_input:
        st.warning("Please enter some text")
    else:
        with st.spinner("Thinking..."):

            # --- CALL YOUR API HERE ---
            response = requests.post(
                "http://127.0.0.1:8000/decision",
                json={"user_input": user_input}
            )

            result = response.json()

        # --- Output ---
        st.divider()

        if result.get("status") == "failed":
            st.error("Something went wrong")
        else:
            data = result.get("data", {})

            st.subheader("🎯 Goal")
            st.write(data.get("goal"))

            st.subheader("⚠️ Constraints")
            for c in data.get("constraints", []):
                st.write(f"- {c}")

            st.subheader("🧩 Options")
            for opt in data.get("options", []):
                st.write(f"**{opt}**")

                pros = data["pros_cons"][opt]["pros"]
                cons = data["pros_cons"][opt]["cons"]

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**✅ Pros**")
                    for p in pros:
                        st.write(f"- {p}")

                with col2:
                    st.markdown("**❌ Cons**")
                    for c in cons:
                        st.write(f"- {c}")

                st.divider()

            st.subheader("➡️ Next Steps")
            for step in data.get("next_steps", []):
                st.write(f"- {step}")

            st.subheader("📊 Meta")
            st.write(f"Provider: {result.get('provider')}")
            st.write(f"Quality: {result.get('quality')}")
            st.write(f"Fallback used: {result.get('fallback')}")