String msg, host, content, contentl, msg_enviar;
 
void setup()
{
  Serial.begin(115200);
  delay(5000);
  Serial.println("AT+RST"); //reset wifi
  delay(2000);
  Serial.println("AT+CWMODE=3");  //station mode
  delay(1000);
   //connect to AP, ADD YOUR ROUTER SSID and PASSWORD
  Serial.println("AT+CWJAP=\"iPhone do Guto\",\"87654321\"");
  delay(10000);
  
}
 
void loop()
{    
    //GET request of a website page a2.php 
    msg = "POST /sensor/ HTTP/2.0";
    host = "HOST: marbleastrounauts.pythonanywhere.com";  //change to your website address
    content = "Content-Type: application/x-www-form-urlencoded";
    contentl = "Content-Lenght: 5"; 
    msg_enviar = "a0=35";
    
    Serial.println("AT+CIPSTART=\"TCP\",\"marbleastrounauts.pythonanywhere.com\",80\");  //change to your website address
    delay(1000);
    Serial.println("AT+CIPSEND=" + String(msg.length() + host.length() + content.length() + contentl.length() + msg_enviar.length() + 6));
    delay(1000);
    
    Serial.println(msg);
    Serial.println(host);
    Serial.println(content);
    Serial.println(contentl);
    Serial.println(msg_enviar);
    Serial.println("");

    delay(15000);
}
