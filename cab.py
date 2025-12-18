import streamlit as st
import qrcode
from io import BytesIO
import uuid
from gtts import gTTS

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

st.set_page_config(page_title="METRO TICKET BOOKING")
st.title("Metro Ticket Booking System")

stations = ["Ameerpet", "Miyapur", "LB Nagar", "KPHB", "JNTU"]

name = st.text_input("Passenger Name")
source = st.selectbox("Source Station", stations)
destination = st.selectbox("Destination Station", stations)
no_tickets = st.number_input("Number of Tickets", min_value=1, value=1)

price_per_ticket = 30
total_amount = no_tickets * price_per_ticket

st.info("Total Amount: " + str(total_amount))

if st.button("Book Ticket"):

    if name.strip() == "":
        st.error("Please enter passenger name")

    elif source == destination:
        st.error("Source and destination cannot be same")

    else:
        booking_id = str(uuid.uuid4())[:8]

        qr_data = (
            "Booking ID: " + booking_id + "\n"
            "Name: " + name + "\n"
            "From: " + source + "\n"
            "To: " + destination + "\n"
            "Tickets: " + str(no_tickets) + "\n"
            "Amount: " + str(total_amount)
        )

        qr_img = generate_qr(qr_data)
        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes = buf.getvalue()

        st.success("Ticket booked successfully")

        st.write("Ticket Details")
        st.write("Booking ID:", booking_id)
        st.write("From:", source)
        st.write("To:", destination)
        st.write("Tickets:", no_tickets)
        st.write("Amount Paid:", total_amount)

        st.image(qr_bytes, width=250)



