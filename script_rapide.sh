#!/bin/bash
read -n 1 -s -r -p "Appuyez sur Entrée pour lancer les programmes"
echo
/bin/python3 ./Points.py false &
sleep 1
/bin/python3 ./Points.py &
sleep 1
/bin/python3 ./Image.py bleu.jpg rouge.webp  &
sleep 1
/bin/python3 ./Image.py parthenon.jpg space.jpg &
sleep 1
/bin/python3 ./ImageAvecWhitening.py bleu.jpg rouge.webp  &
sleep 1
/bin/python3 ./ImageAvecWhitening.py parthenon.jpg space.jpg &
sleep 1
/bin/python3 ./ImageGradient.py bleu.jpg rouge.webp &
sleep 1
/bin/python3 ./ImageGradient.py parthenon.jpg space.jpg &
sleep 1
read -n 1 -s -r -p "Appuyez sur Entrée pour terminer"
echo
killall python3
echo fin du test

