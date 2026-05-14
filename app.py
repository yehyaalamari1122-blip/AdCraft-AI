import streamlit as st
from google import genai

# Page configuration
st.set_page_config(page_title="AdCraft AI", page_icon="🚀", layout="wide")

# Custom CSS for modern UI
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 AdCraft AI - Marketing Ad Generator")
st.write("Generate high-converting ad copies using Google Gemini AI.")

# Sidebar for API Key
st.sidebar.header("🔑 API Settings")
gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")

# Main layout inputs
col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("Product Name", placeholder="e.g., Smart Watch V2")
    target_audience = st.text_input("Target Audience", placeholder="e.g., Tech enthusiasts, fitness lovers")

with col2:
    platform = st.selectbox("Platform", ["Facebook", "Instagram", "Google Ads", "TikTok"])
    product_description = st.text_area("Product Description", placeholder="Describe your product features and benefits...")

# Generate ads button
if st.button("Generate Ads"):
    if not gemini_api_key:
        st.error("Please enter your Gemini API Key in the sidebar!")
    elif not product_name or not product_description:
        st.error("Please fill in the Product Name and Description!")
    else:
        with st.spinner("Generating your high-converting ads..."):
            try:
                # Create a session client
                client = genai.Client(api_key=gemini_api_key)
                
                # Call the model
                prompt = f"Create 3 high-converting ads for {product_name}. Description: {product_description}. Target Audience: {target_audience}. Platform: {platform}. Include catchy headlines, main body text, engaging emojis, and relevant hashtags."
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                
                # Display the results
                st.success("🎉 Ads generated successfully!")
                st.markdown("### 📋 Generated Ad Copies:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
