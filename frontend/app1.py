import streamlit as st
import requests
import os

# Page configuration
st.set_page_config(
    page_title="Medical Insurance Predictor", 
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API URL configuration
API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000")

# Main title
st.title("🏥 Medical Insurance Price Predictor")
st.markdown("Predict your medical insurance costs based on personal information")

# Create layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📋 Personal Information")
    
    # Input fields
    age = st.slider("Age", min_value=18, max_value=100, value=30, help="Your current age")
    sex = st.selectbox("Gender", ["male", "female"], help="Select your gender")
    bmi = st.number_input(
        "BMI (Body Mass Index)", 
        min_value=10.0, 
        max_value=50.0, 
        value=25.0, 
        step=0.1,
        help="Your Body Mass Index"
    )
    children = st.number_input(
        "Number of Children", 
        min_value=0, 
        max_value=10, 
        value=0, 
        step=1,
        help="Number of dependent children"
    )
    smoker = st.selectbox("Smoking Status", ["no", "yes"], help="Do you smoke?")
    region = st.selectbox(
        "Region", 
        ["northeast", "northwest", "southeast", "southwest"],
        help="Your geographical region"
    )

with col2:
    st.header("🔮 Prediction")
    
    # Prediction button
    predict_button = st.button(
        "🔍 Predict Insurance Cost", 
        type="primary",
        use_container_width=True
    )
    
    # API status check
    st.markdown("### 🌐 API Status")
    try:
        health_res = requests.get(f"{API_URL}/health", timeout=5)
        if health_res.status_code == 200:
            st.success("✅ API: Online")
        else:
            st.error("❌ API: Issues")
    except:
        st.error("❌ API: Offline")
    
    st.markdown(f"**API URL:** `{API_URL}`")

# Prediction logic
if predict_button:
    # Prepare input data
    input_data = {
        "age": float(age),
        "sex": sex,
        "bmi": float(bmi),
        "children": int(children),
        "smoker": smoker,
        "region": region
    }
    
    try:
        with st.spinner("🔄 Calculating your insurance cost..."):
            # Make API request
            response = requests.post(
                f"{API_URL}/predict", 
                json=input_data, 
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result["predicted_insurance_charge"]
                
                # Display results
                st.balloons()  # Celebration animation
                
                # Results section
                st.markdown("---")
                st.header("💰 Prediction Results")
                
                # Main prediction display
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "Annual Cost", 
                        f"₹{prediction:,.2f}",
                        help="Estimated annual insurance premium"
                    )
                
                with col2:
                    monthly_cost = prediction / 12
                    st.metric(
                        "Monthly Cost", 
                        f"₹{monthly_cost:,.2f}",
                        help="Estimated monthly premium"
                    )
                
                with col3:
                    daily_cost = prediction / 365
                    st.metric(
                        "Daily Cost", 
                        f"₹{daily_cost:.2f}",
                        help="Estimated daily cost"
                    )
                
                # Input summary
                st.markdown("### 📊 Input Summary")
                summary_col1, summary_col2 = st.columns(2)
                
                with summary_col1:
                    st.write(f"**Age:** {age} years")
                    st.write(f"**Gender:** {sex.title()}")
                    st.write(f"**BMI:** {bmi}")
                
                with summary_col2:
                    st.write(f"**Children:** {children}")
                    st.write(f"**Smoker:** {smoker.title()}")
                    st.write(f"**Region:** {region.title()}")
                
            else:
                st.error(f"❌ API Error: {response.status_code}")
                st.error(f"Details: {response.text}")
                
    except requests.exceptions.ConnectionError:
        st.error("❌ **Connection Error**")
        st.error("Cannot connect to the prediction service. Please check if the backend is running.")
        st.info(f"Trying to connect to: {API_URL}")
        
    except requests.exceptions.Timeout:
        st.error("⏱️ **Timeout Error**")
        st.error("The request took too long. Please try again.")
        
    except Exception as e:
        st.error(f"❌ **Unexpected Error**")
        st.error(f"Details: {str(e)}")

# Information section
st.markdown("---")
st.markdown("### ℹ️ About This Predictor")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.info("""
    **Factors Affecting Insurance Cost:**
    - **Age**: Older individuals typically have higher premiums
    - **BMI**: Higher BMI may indicate health risks
    - **Smoking**: Significantly increases insurance costs
    - **Region**: Different areas have varying healthcare costs
    - **Children**: Number of dependents affects family coverage
    """)

with info_col2:
    st.warning("""
    **Important Notes:**
    - This is an estimate based on historical data
    - Actual premiums may vary by insurance company
    - Consider this as a reference, not final pricing
    - Consult with insurance providers for accurate quotes
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built with ❤️ using FastAPI & Streamlit | Machine Learning Model: Random Forest"
    "</div>", 
    unsafe_allow_html=True
)