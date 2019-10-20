int pin_mq4 = A0;
int pin_mq7 = A1;
int pin_mq135 = A2;
int pin_LED4 = 9;
int pin_LED7 = 10;
int pin_LED135 = 11;

int nivel_sensor4 = 450;
int nivel_sensor7 = 450;
int nivel_sensor135 = 350;

void setup()
{
  // Define os pinos de leitura do sensor como entrada
  pinMode(pin_mq4, INPUT);
  pinMode(pin_mq7, INPUT);
  pinMode(pin_mq135, INPUT);
  pinMode(pin_LED4, OUTPUT);
  pinMode(pin_LED7, OUTPUT);
  pinMode(pin_LED135, OUTPUT);
  // Inicializa a serial
  Serial.begin(9600);
}

void loop()
{
 float valor_mq4 = 0;
 float valor_mq7 = 0;
 float valor_mq135 = 0;
 
  // Le os dados dos pinos analogicos do sensor
 for (int i = 0; i <= 999; i ++){
 valor_mq4 += analogRead(pin_mq4);
 valor_mq7 += analogRead(pin_mq7);
 valor_mq135 += analogRead(pin_mq135);
 }
  valor_mq4 /= 1000;
  valor_mq7 /= 1000;
  valor_mq135 /= 1000;
  
  // Mostra os dados no serial monitor
  Serial.print("Gas natural e metano: ");
  Serial.println(valor_mq4);
  Serial.print("Monoxido de carbono: ");
  Serial.println(valor_mq7);
  Serial.print("Gases nocivos a qualidade do ar: ");
  Serial.println(valor_mq135);

  if (valor_mq4 > nivel_sensor4)
  {
    digitalWrite(pin_LED4, HIGH);
  }
  else
  {
    digitalWrite(pin_LED4, LOW);
  }
  
    if (valor_mq7 > nivel_sensor7)
  {
    digitalWrite(pin_LED7, HIGH);
  }
  else
  {
    digitalWrite(pin_LED7, LOW);
  }

    if (valor_mq135 > nivel_sensor135)
  {
    digitalWrite(pin_LED135, HIGH);
  }
  else
  {
    digitalWrite(pin_LED135, LOW);
  }
}
