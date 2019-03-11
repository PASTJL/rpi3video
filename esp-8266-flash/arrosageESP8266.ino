/**
 * BasicHTTPClient.ino
 *
 *  Created on: 24.05.2015
 *
 */

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <ESP8266HTTPClient.h>

//#define USE_SERIAL Serial

ESP8266WiFiMulti WiFiMulti;

void setup() {
    pinMode(1, OUTPUT); 
     digitalWrite(1, LOW);
      pinMode(LED_BUILTIN, OUTPUT); 
     digitalWrite(LED_BUILTIN, LOW);
  //  USE_SERIAL.begin(115200);
   // USE_SERIAL.setDebugOutput(true);

  //  USE_SERIAL.println();
 //   USE_SERIAL.println();
  //  USE_SERIAL.println();

    for(uint8_t t = 4; t > 0; t--) {
     //   USE_SERIAL.printf("[SETUP] WAIT %d...\n", t);
      //  USE_SERIAL.flush();
        delay(1000);
    }
     // Remplacer le <nom de votre reseau> et le <mot de passe> ci-dessous :
	//	 Nom réseau = nom de la box , mot de passe = mot de passe WPA en général 26 caracteres choisis parmi 0123456789ABCDEF
    WiFiMulti.addAP("<nom de votre reseau>", "<mot de passe>");

}

void loop() {
    // wait for WiFi connection
    if((WiFiMulti.run() == WL_CONNECTED)) {

        HTTPClient http;

        // USE_SERIAL.print("[HTTP] begin...\n");
        // configure traged server and url
        //http.begin("https://192.168.1.12/test.html", "7a 9c f4 db 40 d3 62 5a 6e 21 bc 5c cc 66 c8 3e a1 45 59 38"); //HTTPS
       // Verifier le nom DNS donné par votre box a  votre raspberry ( pour moi raspberrypi)  lors de la creation de l'adresse fixe
        // ainsi que le port du virtual host 8853  à configurer dans les fichiers apache 2 :
        //  - /etc/apache2/sites-available/000-default.conf ( virtualhost port 8853 mais on peut choir un autre port autre que 80 et 8080 ) 
        //  - /etc/apache2/ports.conf ( Listen 8853) 
        http.begin("http://raspberrypi:8853/arrosage.cam"); //HTTP

        // USE_SERIAL.print("[HTTP] GET...\n");
        // start connection and send HTTP header
        int httpCode = http.GET();

        // httpCode will be negative on error
        if(httpCode > 0) {
          // HTTP header has been send and Server response header has been handled
          //  USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);

          // file found at server
            if(httpCode == HTTP_CODE_OK) {
               digitalWrite(1, HIGH);
               digitalWrite(LED_BUILTIN,LOW);
              //  USE_SERIAL.printf("[HTTP] GET... codeOK: %d\n", httpCode);
                 
              //String payload = http.getString();
              // USE_SERIAL.println(payload);
              
            }
            else
            {
               digitalWrite(1, LOW);
               digitalWrite(LED_BUILTIN,HIGH);
              //   USE_SERIAL.printf("[HTTP] GET... codeKO: %d\n", httpCode);
                 
            }
        } else {
         //   USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
            digitalWrite(1, LOW);
            digitalWrite(LED_BUILTIN, HIGH);
        }

        http.end();
    }

    delay(2000);
}
