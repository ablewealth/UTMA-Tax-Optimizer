import streamlit as st
import pandas as pd
import json
import streamlit_authenticator as st_auth

# --- App Configuration ---
st.set_page_config(
    page_title="UTMA/UGMA Tax Optimization 2025",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Authentication ---
# For production use, consider loading users from a secure source
users = {
    "usernames": {
        "johndoe": {
            "name": "John Doe",
            "password": "password123", # In a real app, hash this password
        },
        "janesmith": {
            "name": "Jane Smith",
            "password": "password456", # In a real app, hash this password
        },
    }
}

authenticator = st_auth.Authenticate(
    users,
    "utma_tax_optimizer_cookie",
    "a_random_signature_key", # Replace with a real secret key
    cookie_expiry_days=30,
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    # --- Sidebar ---
    st.sidebar.title(f"Welcome, {name}!")
    authenticator.logout("Logout", "sidebar")

    st.sidebar.title("Navigation")
    step = st.sidebar.radio(
        "Go to", ["Account Info", "Holdings", "Optimization"]
    )

    # --- Preset Example ---
    def load_example():
        st.session_state["account_id"] = "ACCT-1001"
        st.session_state["ytd_income"] = 1200.50
        st.session_state["positions"] = pd.DataFrame(
            [
                {"symbol": "AAPL", "unrealized_gain": 500, "quantity": 10},
                {"symbol": "GOOGL", "unrealized_gain": 800, "quantity": 5},
            ]
        )
        st.session_state["tax_year"] = "2025"

    st.sidebar.button("Load Example", on_click=load_example)
    st.sidebar.markdown("---")
    st.sidebar.info("Tip: Use the sidebar to navigate steps. Use 'Load Example' for a demo.")


    # --- Step 1: Account Info ---
    if step == "Account Info":
        st.title("Step 1: Enter Account Info")
        st.text_input("Account ID", key="account_id")
        st.number_input(
            "YTD Realized Income ($)", min_value=0.0, step=0.01, key="ytd_income"
        )
        st.selectbox("Tax Year", ["2025", "2026"], key="tax_year")

    # --- Step 2: Holdings ---
    if step == "Holdings":
        st.title("Step 2: Enter Holdings")
        st.info("Use the table below to add or edit your current positions with unrealized gains.")
        # Initialize dataframe in session state if it doesn't exist
        if "positions" not in st.session_state:
            st.session_state["positions"] = pd.DataFrame(
                columns=["symbol", "unrealized_gain", "quantity"]
            )
        # Use data_editor for a better user experience
        st.session_state["positions"] = st.data_editor(
            st.session_state["positions"],
            num_rows="dynamic",
            column_config={
                "unrealized_gain": st.column_config.NumberColumn(
                    "Unrealized Gain ($)",
                    help="The total unrealized capital gain for this position.",
                    format="$%d",
                )
            }
        )

    # --- Step 3: Optimization ---
    if step == "Optimization":
        st.title("Step 3: Optimization Results")
        # Retrieve data from session state
        account_id = st.session_state.get("account_id", "")
        ytd_income = st.session_state.get("ytd_income", 0.0)
        tax_year = st.session_state.get("tax_year", "2025")
        positions_df = st.session_state.get("positions", pd.DataFrame())

        if not account_id or positions_df.empty:
            st.warning(
                "Please complete 'Account Info' and 'Holdings' steps first."
            )
        else:
            with st.container(border=True):
                col1, col2 = st.columns(2)
                col1.metric("Account ID", account_id)
                col2.metric("Tax Year", tax_year)
                st.metric("Year-to-Date Realized Income", f"${ytd_income:,.2f}")
            
            st.subheader("Current Holdings")
            st.dataframe(positions_df)

            # --- Insert your optimization logic here ---
            # This is a placeholder for your actual tax optimization logic.
            # For example, you could calculate how much gain to realize
            # to stay within a certain tax bracket.
            st.success("Optimization complete! (Results would be displayed here)")

elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password to continue.")
