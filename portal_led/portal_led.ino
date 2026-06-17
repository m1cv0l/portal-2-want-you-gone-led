// Portal 2 - Want You Gone 

const int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9};
const int numLeds = 8;

unsigned long startTime = 0;
unsigned long previousMillis = 0;
int currentMode = 0;        // 0=off, 1=all on, 2=chaser normal, 3=chaser fast, 4=blink fast, 5=blink slow
int chaserSpeed = 110;
int pos = 0;

void setup() {
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  
  startTime = millis();
  turnAllOff();
  
  // Начало: 2 моргания
  blinkAll(2, 300);
  delay(400);
  
  currentMode = 2; // начинаем крутиться по кругу
}

void turnAllOff() {
  for (int i = 0; i < numLeds; i++) digitalWrite(ledPins[i], LOW);
}

void turnAllOn() {
  for (int i = 0; i < numLeds; i++) digitalWrite(ledPins[i], HIGH);
}

void blinkAll(int times, int delayMs) {
  for (int t = 0; t < times; t++) {
    turnAllOn();
    delay(delayMs);
    turnAllOff();
    delay(delayMs);
  }
}

void loop() {
  unsigned long currentTime = millis() - startTime;  // время от старта в миллисекундах

  // === ТАЙМИНГИ ЭФФЕКТОВ ===
  if (currentTime < 24000) {
    currentMode = 2;           // обычный чейзер
    chaserSpeed = 110;
  } 
  else if (currentTime < 41000) {
    currentMode = 1;           // 24 сек — все горят
  } 
  else if (currentTime < 57000) {
    currentMode = 4;           // 41 сек — быстрое мигание
  } 
  else if (currentTime < 65000) {
    currentMode = 0;           // 57 сек — выключено
  } 
  else if (currentTime < 82000) {
    currentMode = 3;           // 1:05 — быстрый чейзер
    chaserSpeed = 50;
  } 
  else if (currentTime < 88000) {
    currentMode = 0;           // 1:22 — выключено
  } 
  else if (currentTime < 97000) {
    currentMode = 5;           // 1:28 — медленное моргание
  } 
  else if (currentTime < 123000) {
    currentMode = 2;           // 1:37 — обычный чейзер
    chaserSpeed = 110;
  } 
  else if (currentTime < 132000) {
    currentMode = 5;           // 2:03 — медленное моргание
  } 
  else {
    currentMode = 1;           // 2:12 — все горят до конца
  }

  // В начале
  unsigned long currentMillis = millis();

  if (currentMode == 0) {                    // Выключено
    turnAllOff();
  } 
  else if (currentMode == 1) {               // Все горят
    turnAllOn();
  } 
  else if (currentMode == 2 || currentMode == 3) { // Чейзер
    if (currentMillis - previousMillis >= chaserSpeed) {
      previousMillis = currentMillis;
      turnAllOff();
      digitalWrite(ledPins[pos], HIGH);
      pos = (pos + 1) % numLeds;
    }
  } 
  else if (currentMode == 4) {               // Быстрое мигание
    if (currentMillis - previousMillis >= 150) {
      previousMillis = currentMillis;
      static bool state = false;
      state = !state;
      for (int i = 0; i < numLeds; i++) digitalWrite(ledPins[i], state ? HIGH : LOW);
    }
  } 
  else if (currentMode == 5) {               // Медленное мигание
    if (currentMillis - previousMillis >= 600) {
      previousMillis = currentMillis;
      static bool state = false;
      state = !state;
      for (int i = 0; i < numLeds; i++) digitalWrite(ledPins[i], state ? HIGH : LOW);
    }
  }

  // конец
  if (currentTime > 147000) {
    turnAllOff();
    while(true); // остановка
  }
}