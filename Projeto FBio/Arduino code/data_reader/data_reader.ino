const int ledPin = 8;
const int buttonPin = 2;
bool game_active = true;

void setup() {
 Serial.begin(9600);
 pinMode(ledPin, OUTPUT);
 pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    if (data == "game_not_active") {
      game_active = false;
    }
    if (data == "game_active") {
      game_active = true;
    }
    
    // Check received data and perform actions
    if (data == "LED_ON") {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
    } else if (data == "LED_OFF") {
      digitalWrite(ledPin, LOW);   // Turn off the LED
    }
     data = "";
  }

  if (game_active) {
    Serial.println(analogRead(A0));
    delay(10);
  }

  if (not game_active) {
    if (digitalRead(buttonPin) == HIGH) {
      // Button is pressed, send 'S' to indicate game start
      Serial.println('S');
      // You can add a delay to avoid sending 'S' multiple times while the button is held down
      // Adjust the delay time as needed
      
    }
  }
  
}
