#!/usr/bin/env python3
"""
Motor Test Script für L298N mit 2 DC Motoren
Raspberry Pi GPIO Pins: 17, 18, 27, 22

Pin-Belegung:
- Motor A (Links):  IN1=17, IN2=18
- Motor B (Rechts): IN3=27, IN4=22

Hinweis: Falls Enable-Pins (ENA, ENB) vorhanden, 
         auf dem L298N mit Jumper brücken für volle Geschwindigkeit
         ODER separate PWM-Pins verwenden
"""

import RPi.GPIO as GPIO
import time
import sys

# GPIO Pin Definitionen
MOTOR_LEFT_IN1 = 17   # Motor A - IN1
MOTOR_LEFT_IN2 = 18   # Motor A - IN2
MOTOR_RIGHT_IN3 = 27  # Motor B - IN3
MOTOR_RIGHT_IN4 = 22  # Motor B - IN4

# Setup
def setup():
    """GPIO Setup"""
    GPIO.setmode(GPIO.BCM)  # BCM Pin-Nummerierung
    GPIO.setwarnings(False)
    
    # Alle Pins als Output
    GPIO.setup(MOTOR_LEFT_IN1, GPIO.OUT)
    GPIO.setup(MOTOR_LEFT_IN2, GPIO.OUT)
    GPIO.setup(MOTOR_RIGHT_IN3, GPIO.OUT)
    GPIO.setup(MOTOR_RIGHT_IN4, GPIO.OUT)
    
    # Alle Pins initial auf LOW
    GPIO.output(MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_IN2, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_IN3, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_IN4, GPIO.LOW)
    
    print("✓ GPIO Setup complete")
    print(f"  Motor Left:  IN1={MOTOR_LEFT_IN1}, IN2={MOTOR_LEFT_IN2}")
    print(f"  Motor Right: IN3={MOTOR_RIGHT_IN3}, IN4={MOTOR_RIGHT_IN4}")
    print()

# Motor-Steuerungsfunktionen
def motor_left_forward():
    """Motor Links vorwärts"""
    GPIO.output(MOTOR_LEFT_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_IN2, GPIO.LOW)

def motor_left_backward():
    """Motor Links rückwärts"""
    GPIO.output(MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_IN2, GPIO.HIGH)

def motor_left_stop():
    """Motor Links stoppen"""
    GPIO.output(MOTOR_LEFT_IN1, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_IN2, GPIO.LOW)

def motor_right_forward():
    """Motor Rechts vorwärts"""
    GPIO.output(MOTOR_RIGHT_IN3, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_IN4, GPIO.LOW)

def motor_right_backward():
    """Motor Rechts rückwärts"""
    GPIO.output(MOTOR_RIGHT_IN3, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_IN4, GPIO.HIGH)

def motor_right_stop():
    """Motor Rechts stoppen"""
    GPIO.output(MOTOR_RIGHT_IN3, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_IN4, GPIO.LOW)

def motors_stop():
    """Beide Motoren stoppen"""
    motor_left_stop()
    motor_right_stop()

# Test-Funktionen
def test_gegenlaeufig():
    """
    Test: Motoren gegenläufig
    Links vorwärts, Rechts rückwärts → Drehung nach rechts
    """
    print("TEST 1: Gegenläufig - Drehung nach RECHTS")
    print("  Links: Vorwärts, Rechts: Rückwärts")
    
    motor_left_forward()
    motor_right_backward()
    time.sleep(2)
    motors_stop()
    
    print("  → Motoren gestoppt")
    time.sleep(1)
    print()

def test_gegenlaeufig_links():
    """
    Test: Motoren gegenläufig andersrum
    Links rückwärts, Rechts vorwärts → Drehung nach links
    """
    print("TEST 2: Gegenläufig - Drehung nach LINKS")
    print("  Links: Rückwärts, Rechts: Vorwärts")
    
    motor_left_backward()
    motor_right_forward()
    time.sleep(2)
    motors_stop()
    
    print("  → Motoren gestoppt")
    time.sleep(1)
    print()

def test_beide_vorwaerts():
    """
    Test: Beide Motoren vorwärts
    Fahrzeug sollte geradeaus fahren
    """
    print("TEST 3: Beide Motoren VORWÄRTS")
    print("  Fahrzeug sollte geradeaus fahren")
    
    motor_left_forward()
    motor_right_forward()
    time.sleep(2)
    motors_stop()
    
    print("  → Motoren gestoppt")
    time.sleep(1)
    print()

def test_beide_rueckwaerts():
    """
    Test: Beide Motoren rückwärts
    Fahrzeug sollte rückwärts fahren
    """
    print("TEST 4: Beide Motoren RÜCKWÄRTS")
    print("  Fahrzeug sollte rückwärts fahren")
    
    motor_left_backward()
    motor_right_backward()
    time.sleep(2)
    motors_stop()
    
    print("  → Motoren gestoppt")
    time.sleep(1)
    print()

def test_einzeln_links():
    """Test: Nur linker Motor"""
    print("TEST 5: Nur LINKER Motor")
    print("  Vorwärts...")
    motor_left_forward()
    time.sleep(1.5)
    motor_left_stop()
    
    time.sleep(0.5)
    
    print("  Rückwärts...")
    motor_left_backward()
    time.sleep(1.5)
    motor_left_stop()
    
    print("  → Motor gestoppt")
    time.sleep(1)
    print()

def test_einzeln_rechts():
    """Test: Nur rechter Motor"""
    print("TEST 6: Nur RECHTER Motor")
    print("  Vorwärts...")
    motor_right_forward()
    time.sleep(1.5)
    motor_right_stop()
    
    time.sleep(0.5)
    
    print("  Rückwärts...")
    motor_right_backward()
    time.sleep(1.5)
    motor_right_stop()
    
    print("  → Motor gestoppt")
    time.sleep(1)
    print()

def test_wechsel():
    """Test: Schneller Richtungswechsel"""
    print("TEST 7: Schneller Richtungswechsel")
    
    for i in range(3):
        print(f"  Zyklus {i+1}/3: Vorwärts → Rückwärts")
        
        motor_left_forward()
        motor_right_forward()
        time.sleep(0.5)
        motors_stop()
        time.sleep(0.2)
        
        motor_left_backward()
        motor_right_backward()
        time.sleep(0.5)
        motors_stop()
        time.sleep(0.2)
    
    print("  → Test abgeschlossen")
    time.sleep(1)
    print()

def cleanup():
    """GPIO Cleanup"""
    motors_stop()
    GPIO.cleanup()
    print("✓ GPIO Cleanup complete")

# Hauptprogramm
def main():
    """Hauptprogramm - führt alle Tests aus"""
    
    print("=" * 60)
    print("MOTOR TEST SCRIPT - L298N mit 2 DC Motoren")
    print("=" * 60)
    print()
    print("WICHTIG:")
    print("  - Fahrzeug sollte auf Böcken stehen oder Räder frei drehen!")
    print("  - Stromversorgung für Motoren angeschlossen?")
    print("  - Enable-Pins (ENA, ENB) gebrückt oder mit PWM?")
    print()
    
    response = input("Bereit für Test? (Enter = Ja, Ctrl+C = Abbruch): ")
    print()
    
    try:
        # Setup
        setup()
        
        # Tests durchführen
        test_gegenlaeufig()          # Test 1: Gegenläufig rechts
        test_gegenlaeufig_links()    # Test 2: Gegenläufig links
        test_beide_vorwaerts()       # Test 3: Beide vorwärts
        test_beide_rueckwaerts()     # Test 4: Beide rückwärts
        test_einzeln_links()         # Test 5: Links einzeln
        test_einzeln_rechts()        # Test 6: Rechts einzeln
        test_wechsel()               # Test 7: Richtungswechsel
        
        print("=" * 60)
        print("ALLE TESTS ABGESCHLOSSEN!")
        print("=" * 60)
        print()
        print("Beobachtungen:")
        print("  - Drehen beide Motoren in die richtige Richtung?")
        print("  - Sind sie gleich schnell?")
        print("  - Gibt es unerwartete Geräusche?")
        print()
        
    except KeyboardInterrupt:
        print()
        print("Test durch Benutzer abgebrochen (Ctrl+C)")
        
    except Exception as e:
        print()
        print(f"FEHLER: {e}")
        
    finally:
        cleanup()

if __name__ == "__main__":
    main()
