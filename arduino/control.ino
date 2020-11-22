const int ledPin = 9; // the pin that the LED is attached to

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

String handleCommand() {
  String command = "";
  char curChar = Serial.read();
  while(curChar != '\n' && Serial.available() > 0) {
    command += curChar;
    curChar = Serial.read();
  }
  exeCommand(command);
}

void exeCommand(String command) {
   //Serial.println("Executing command...");
   if (command.equals("HIGH")) {
     digitalWrite(ledPin, HIGH);
     Serial.write('S'); //success
   } else if (command.equals("LOW")) {
     digitalWrite(ledPin, LOW);
     Serial.write('S'); //success
   } else {
     Serial.write('F');
   }
}

void loop() {
  // see if there's incoming serial data:
  if(Serial.available() > 0) {
    //delay to allow all of the bytes of the command to finish coming across
    delay(500);
    handleCommand();
    //delay to allow all of the bytes of the command to be read
    delay(200);
  }
}