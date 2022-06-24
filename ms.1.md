# Start af program
Efter at have tilsluttet Raspberry Pi’en til strøm, kører programmet, og der udskrives en “Program Starting” besked efterfulgt af en blå skærm.

# Start af ur
For at sætte uret i gang, skub joysticket i en retning (op, ned, højre, venstre), dette vil starte uret. Som standard starter uret i seks cifret form 12 timer, for at få trecifret 12 timer, rotor raspberry pi’en så ledningen peger nedad, vil du have 6 cifre 24 timer, drej raspberry pi’en så ledningen peger op, og 3 cifre 24 timer, drej så ledningen peger mod venstre.

# Slukke / Afbryde systemet
For at slukke / afbryde systemet, skal du trykke joysticket nedad, det vil udskrive en “Program finishing” besked, og derefter lukker programmet.

# Enabling af service
sudo chmod 644 /lib/systemd/system/main.service
chmod +x /home/pi/main.py
sudo systemctl daemon-reload
sudo systemctl enable main.service
sudo systemctl start main.service

# Slukning af service
sudo systemctl stop main.service