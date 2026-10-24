int baseline = 1489; // Neutral stick/channel center point

const int CH1 = 11;  // Receiver Channel 1 input pin
const int CH2 = 10;  // Receiver Channel 2 input pin

void setup() {
  Serial.begin(115200); // Initialize serial communication
  delay(2000);          // Brief startup pause
}

void loop() {
    
   // Read incoming PWM pulse widths (timeout after 30ms)
   float y = pulseIn(CH2, HIGH, 30000);
   float x = pulseIn(CH1, HIGH, 30000);
  
   // Mix X based on Y's offset from the baseline
   if(y > baseline){
      int a = y - baseline;
      x = x + a;
   } else if(y < baseline){
     int a = baseline - y;
     x = x - a;
   }
  
   // Cross-mix Y based on X's offset within specific thresholds
   if(x < baseline && y >= 1480){
     int b = baseline - x;
     y = y + b;
   } else if(x > baseline && y <= 1510){
     int b = x - baseline;
     y = y - b;
   }

   // Scale and convert raw receiver data into usable values for the CRICKIT HAT
   Serial.println(String(((x * pow(10, -4)) * 3) - 0.45)); 
   Serial.println(String(((y * pow(10, -4)) * 3) - 0.45));
}
