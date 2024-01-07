#include <AccelStepper.h>

#include <ESP8266WiFi.h>
String receivedMessage;
const char* ssid = "robotics_2";       // Replace with your local Wi-Fi network name
const char* password = "CLB422BFB0"; // Replace with your local Wi-Fi password
const char* server_ip = "192.168.1.77";   // Replace with your laptop"s IP address
const int server_port = 12345;        // Choose a port number

WiFiClient client;

const int stepsPerRevolution = 2048;  // change this to fit the number of steps per revolution

// ULN2003 Motor Driver Pins
#define IN1 16 // D1
#define IN2 15// D2
#define IN3 14 //D5
#define IN4 0 // D6

#define IN5 12 // RX
#define IN6 13// TX
#define IN7 3 // D7
#define IN8 1 // D8

// initialize the stepper library
AccelStepper stepper1(AccelStepper::FULL4WIRE, IN1, IN3, IN2, IN4);
AccelStepper stepper2(AccelStepper::FULL4WIRE, IN5, IN7, IN6, IN8);

void setup() {
  delay(2000);
  // initialize the serial port
  Serial.begin(115200);
  
  // set the speed and acceleration
  stepper1.setMaxSpeed(600);
  stepper1.setAcceleration(100);


    // set the speed and acceleration
  stepper2.setMaxSpeed(600);
  stepper2.setAcceleration(100);


    // Connect to local Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Connect to the server
  Serial.println("Connecting to server...");
  while (!client.connect(server_ip, server_port)) {
    Serial.println("Connection failed. Retrying...");
    delay(1000);
  }
  Serial.println("Connected to server");
}


void loop() {

  client.print("Hello Server!");
  // // Wait for a response from the server
  //new
  while (client.available() > 0) {
    receivedMessage += (char)client.read();
    Serial.print("recieved");
    Serial.println(receivedMessage);
  }
  String command = receivedMessage.substring(0, receivedMessage.indexOf(":"));
  int stepsPerRevolution = receivedMessage.substring(receivedMessage.indexOf(":") + 1).toInt();

  delay(500);
    // Check the command and adjust the direction accordingly
    if (command == "F" || command == "f") {
      // Move forward
      stepper1.moveTo(stepsPerRevolution);
      stepper2.moveTo(stepsPerRevolution);
      Serial.println("Moving Forward");
      // client.print("Moving Forward");
    } 
    else if (command == "B" || command == "b") {
      // Move backward
      stepper1.moveTo(-stepsPerRevolution);
      stepper2.moveTo(-stepsPerRevolution);
      Serial.println("Moving Backward");
      // client.print("Moving Backward");
    }
    else if (command == "L" || command == "l"){
      stepper1.moveTo(stepsPerRevolution);
      stepper2.moveTo(-stepsPerRevolution);
      Serial.println("Moving Left");
      // client.print("Moving Left");
    }
    else if (command == "R" || command == "r"){
      stepper1.moveTo(-stepsPerRevolution);
      stepper2.moveTo(stepsPerRevolution);
      Serial.println("Moving Right");
      // client.print("Moving Right");
    }
    else if (command == "S" || command == "s"){
      stepper1.stop();
      stepper2.stop();
      stepper1.setCurrentPosition(0);
      stepper2.setCurrentPosition(0);    
      Serial.println("STOP!");
    }
  
  // move the stepper motor (one step at a time)
  stepper1.run();
  stepper2.run();
  
}
