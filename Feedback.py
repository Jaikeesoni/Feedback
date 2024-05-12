import streamlit as st
st.title('Enhanced User Interaction and Feedback')

feedback = st.text_area("Feedback on our app:")
submit = st.button("Submit Feedback")
if submit:
    with st.spinner('Processing...'):
        st.success('Thank you for your feedback!')
if st.checkbox("I agree to participate in interaction tracking"):
    st.session_state.user_agreed = True
    st.write("Thank you for helping us improve!")
else:
    st.session_state.user_agreed = False
