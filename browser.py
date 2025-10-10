import streamlit as st

# ------------------- Vehicle Classes -------------------
class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting"

class car(vehicle):
    def play_music(self):
        return f"{self.brand} {self.model} turns on music"

class electric_vehicle(car):
    def charge(self):
        return f"{self.brand} {self.model} is on charge"

class smart_device:
    def __init__(self, wifi="WiFi"):
        self.wifi = wifi

    def connect_wifi(self):
        return f"{self.brand} {self.model} is connected to {self.wifi}"

class smart_car(car, smart_device):
    def __init__(self, brand, model, wifi="WiFi"):
        car.__init__(self, brand, model)
        smart_device.__init__(self, wifi)

    def auto_drive(self):
        return f"{self.brand} {self.model} is on auto driving mode."

class bike(vehicle):
    def kick_start(self):
        return f"{self.brand} {self.model} is kick started"

class electric_smartcar(smart_car, electric_vehicle):
    def __init__(self, brand, model, wifi="WiFi"):
        electric_vehicle.__init__(self, brand, model)
        smart_device.__init__(self, wifi)

    def autopilot_mode(self):
        return f"{self.brand} {self.model} is on auto pilot mode"

# ------------------- Streamlit UI -------------------
st.set_page_config(page_title="Vehicle System")
st.title(" Vehicle Management System")

col1, col2 = st.columns([2, 1])

with col1:
    vehicle_type = st.selectbox(
        "Select Vehicle Type",
        ["Vehicle", "Car", "Electric Vehicle", "Smart Car", "Bike", "Electric Smart Car"]
    )

    brand = st.text_input("Enter Brand Name")
    model = st.text_input("Enter Model Name")

    if st.button("Submit"):
        if not brand or not model:
            st.warning("Please enter both Brand and Model")
        else:
            if vehicle_type == "Vehicle":
                v = vehicle(brand, model)
                st.success(v.start())

            elif vehicle_type == "Car":
                c = car(brand, model)
                st.success(c.start())
                st.info(c.play_music())

            elif vehicle_type == "Electric Vehicle":
                ev = electric_vehicle(brand, model)
                st.success(ev.start())
                st.info(ev.play_music())
                st.info(ev.charge())

            elif vehicle_type == "Smart Car":
                sc = smart_car(brand, model)
                st.success(sc.start())
                st.info(sc.connect_wifi())
                st.info(sc.auto_drive())

            elif vehicle_type == "Bike":
                b = bike(brand, model)
                st.success(b.start())
                st.info(b.kick_start())

            elif vehicle_type == "Electric Smart Car":
                esc = electric_smartcar(brand, model)
                st.success(esc.start())
                st.info(esc.play_music())
                st.info(esc.connect_wifi())
                st.info(esc.charge())
                st.info(esc.autopilot_mode())

with col2:
    st.subheader("Car Features")
    if vehicle_type == "Vehicle":
        st.write("- Start")
    elif vehicle_type == "Car":
        st.write("- Start\n- Play Music")
    elif vehicle_type == "Electric Vehicle":
        st.write("- Start\n- Play Music\n- Charge")
    elif vehicle_type == "Smart Car":
        st.write("- Start\n- Connect Wifi\n- Auto Drive")
    elif vehicle_type == "Bike":
        st.write("- Start\n- Kick Start")
    elif vehicle_type == "Electric Smart Car":
        st.write("- Start\n- Play Music\n- Connect Wifi\n- Charge\n- Autopilot Mode")