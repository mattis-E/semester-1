# Week 1.2, Session 2: Task 6

temperature = int(input("Machine's temperature (Celsius): "))
pressure = int(input("Machine's pressure (PSI): "))
status = int(input("Machine status (1 = Operating, 0 = Stopped): "))

temp_safe = True
pressure_safe = True
status_operating = True

if temperature > 80:
    print("Temeprature is too high! Shut down the machine.")
    temp_safe = False
elif 50 < temperature < 80:
    print("Temperature is within safe limits.")
else:
    print("Temperature is low; no action needed.")

if pressure > 100:
    print("High pressure detected! Machine requires maintenance.")
    pressure_safe = False
elif 70 < pressure < 100:
    print("Pressure stable.")
else:
    print("Pressure is low; system operating normally.")

if status_operating == 1:
    if not temp_safe or not pressure_safe:
        print("Alert! The machine is running in unsafe conditions and should be shut down.")
    else:
        print("The machine is operating normally.")
else:
    print("The machine is stopped; no action is needed.")