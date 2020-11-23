
const int ledPin = 9; // the pin that the LED is attached to

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

String readCommand() {
  String command = "";
  char curChar = Serial.read();
  while(curChar != '\n' && Serial.available() > 0) {
    command += curChar;
    curChar = Serial.read();
  }
  exeGenericCommand(command);
}

void moveToHomePosition() {

}

void movePenUp() {
  
}

void movePenDown() {
  
}

void exeMovementCommand(String shape, double startx, double starty, double endx, double endy) {
  
}

void exeGenericCommand(String command) {
   //Serial.println("Executing command...");
   if (command.equals("HOME")) {
      moveToHomePosition();
   } else if(command.equals("PENUP")) {
      movePenUp();
   } else if(command.equals("PENDOWN")) {
     movePenDown();
   } else {
     //do something if the command is not understood
   }
}

void loop() {
  // see if there's incoming serial data:
  if(Serial.available() > 0) {
    //delay to allow all of the bytes of the command to finish coming across
    delay(500);
    readCommand();
    //delay to allow all of the bytes of the command to be read
    delay(200);
  }
}