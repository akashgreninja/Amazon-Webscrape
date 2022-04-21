


my_email="Your_email"
other_email="Other person's email"
password="your-gmail-password"
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage


headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

try:
    request=requests.get(url="https://www.amazon.in/herbalife-Mango-Protein-Powder-Afresh/dp/B00TKMAZF4/ref=sr_1_3?crid=YB1X5NAEAOE0&keywords=herbalife&qid=1650563931&sprefix=herballife%2Caps%2C435&sr=8-3",headers=headers)

    # request=requests.get(url="https://www.amazon.in/herbalife-Mango-Protein-Powder-Afresh/dp/B00TKMAZF4/ref=sr_1_3?crid=YB1X5NAEAOE0&keywords=herbalife&qid=1650563931&sprefix=herballife%2Caps%2C435&sr=8-3")
except :
    request=requests.get(url="https://www.amazon.in/herbalife-Mango-Protein-Powder-Afresh/dp/B00TKMAZF4/ref=sr_1_3?crid=YB1X5NAEAOE0&keywords=herbalife&qid=1650563931&sprefix=herballife%2Caps%2C435&sr=8-3",headers=headers)


else:
    data = request.text
    # print(data)
    soup = BeautifulSoup(data, "lxml")
    found=soup.select(selector="div span.a-price-whole")
    # found = soup.find(class_="a-price-whole")
    forza=[i.getText().split(",") for i in found]
    # print(forza)
    forza_final=f"{forza[0][0]}{forza[0][1].strip('.')}"
    # print(final_forza)
    if int(forza_final) <2300:
        msg = EmailMessage()
        msg.set_content(" its cheap ")

        msg['Subject'] = 'it is 2300 order now'
        msg['From'] = my_email
        msg['To'] = other_email

        with smtplib.SMTP('smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login(my_email, password=password)
            server.send_message(msg)

    else:
        print("not today")




