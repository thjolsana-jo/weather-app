import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter City")
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather")

        self.emoji_label = QLabel("")
        self.temperature_label = QLabel("")
        self.description_label = QLabel("")

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Weather App")
        self.resize(350, 450)

      
        self.city_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.get_weather_button.clicked.connect(self.get_weather)

     
        self.card = QWidget()

        self.card.setStyleSheet("""
        QWidget{
            background: rgba(255,255,255,0.15);
            border-radius:20px;
        }
        """)

        card_layout = QVBoxLayout()

        card_layout.addWidget(self.city_label)
        card_layout.addWidget(self.city_input)
        card_layout.addWidget(self.get_weather_button)
        card_layout.addWidget(self.emoji_label)
        card_layout.addWidget(self.temperature_label)
        card_layout.addWidget(self.description_label)

        self.card.setLayout(card_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.card)
        self.setLayout(layout)

   
        self.setStyleSheet("""
        QWidget{
            background:qlineargradient(
                x1:0,y1:0,
                x2:1,y2:1,
                stop:0 #4facfe,
                stop:1 #00f2fe
            );
        }

        QLabel{
            color:white;
            font-family:Segoe UI;
        }

        QLabel#emoji_label{
            font-size:90px;
            font-family:"Segoe UI Emoji";
        }

        QLabel#temperature_label{
            font-size:45px;
            font-weight:bold;
        }

        QLabel#description_label{
            font-size:22px;
        }

        QLineEdit{
            background:rgba(255,255,255,0.7);
            border-radius:10px;
            padding:8px;
            font-size:18px;
        }

        QPushButton{
            background:rgba(255,255,255,0.6);
            border-radius:10px;
            padding:10px;
            font-size:18px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:rgba(255,255,255,0.9);
        }
        """)

        self.emoji_label.setObjectName("emoji_label")
        self.temperature_label.setObjectName("temperature_label")
        self.description_label.setObjectName("description_label")

    def get_weather(self):

        api_key = "aedd236d4d8093cb98f1a33d5b05799f"

        city = self.city_input.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            weather_id = data["weather"][0]["id"]

            self.temperature_label.setText(f"{temp}°C")
            self.description_label.setText(desc.title())

            self.emoji_label.setText(self.get_emoji(weather_id))

        except:
            self.temperature_label.setText("Error")
            self.description_label.setText("City not found")
            self.emoji_label.setText("❌")

    def get_emoji(self, weather_id):

        if weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 200 <= weather_id <= 232:
            return "⛈️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        else:
            return "🌫️"


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WeatherApp()
    window.show()

    sys.exit(app.exec_())