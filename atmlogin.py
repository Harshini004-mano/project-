# atm_inheritance_streamlit.py
import streamlit as st

# -------------------
# Parent class: BankAccount
# -------------------
class BankAccount:
    def __init__(self, account_holder, balance=1000):
        self.account_holder = account_holder
        self._balance = balance  # Protected attribute

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"${amount:.2f} deposited. New balance: ${self._balance:.2f}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"${amount:.2f} withdrawn. New balance: ${self._balance:.2f}"
        elif amount > self._balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

# -------------------
# Child class: ATM
# -------------------
class ATM(BankAccount):
    def __init__(self, account_holder, pin, balance=1000):
        super().__init__(account_holder, balance)
        self.pin = pin

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

# -------------------
# Streamlit App
# -------------------
st.title("ATM Simulation with Inheritance")

# Initialize session state
if 'atm_user' not in st.session_state:
    st.session_state.atm_user = ATM("Raghu", "1234")  # Default user
if 'pin_verified' not in st.session_state:
    st.session_state.pin_verified = False
if 'attempts' not in st.session_state:
    st.session_state.attempts = 3

# PIN verification
if not st.session_state.pin_verified:
    st.write("Enter your 4-digit PIN:")
    entered_pin = st.text_input("PIN", type="default")  # Visible PIN
    if st.button("Verify PIN"):
        if st.session_state.atm_user.verify_pin(entered_pin.strip()):
            st.success("PIN is valid. Access granted.")
            st.session_state.pin_verified = True
        else:
            st.session_state.attempts -= 1
            st.error(f"PIN is invalid. {st.session_state.attempts} attempt(s) remaining.")
            if st.session_state.attempts == 0:
                st.stop()

# ATM operations
if st.session_state.pin_verified:
    option = st.selectbox("Select an option", ["Check Balance", "Deposit Funds", "Withdraw Funds", "Exit"])

    if option == "Check Balance":
        st.info(f"Your current balance is: ${st.session_state.atm_user.check_balance():.2f}")

    elif option == "Deposit Funds":
        deposit = st.number_input("Enter amount to deposit", min_value=0.01, step=0.01)
        if st.button("Deposit"):
            msg = st.session_state.atm_user.deposit(deposit)
            st.success(msg)

    elif option == "Withdraw Funds":
        withdraw = st.number_input("Enter amount to withdraw", min_value=0.01, step=0.01)
        if st.button("Withdraw"):
            msg = st.session_state.atm_user.withdraw(withdraw)
            if "Insufficient" in msg or "Invalid" in msg:
                st.error(msg)
            else:
                st.success(msg)

    elif option == "Exit":
        st.write("Thank you for using the ATM. Goodbye!")
        st.session_state.pin_verified = False
