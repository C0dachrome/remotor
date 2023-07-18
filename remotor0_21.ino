int baseline = 1489;

const int CH1 = 11;
const int CH2 = 10;




void setup() {
  Serial.begin(115200);
  delay(2000);
}

void loop() {
   
   float y = pulseIn(CH2, HIGH, 30000);
   float x = pulseIn(CH1, HIGH, 30000);
  
  if(y > baseline){
     int a = y - baseline;
     x = x + a;
  } else if(y < baseline){
    int a = baseline - y;
    x = x - a;
  }
  
  if(x < baseline && y >= 1480){
    int b = baseline - x;
    y = y + b;
  } else if(x > baseline && y <= 1510){
    int b = x - baseline;
    y = y - b;
  }

  
   Serial.println(String(((x*pow(10,-4))*3)-0.45)); // turns the garbage from the reciever into something the CRICKIT HAT can use.
   Serial.println(String(((y*pow(10,-4))*3)-0.45));
  }
