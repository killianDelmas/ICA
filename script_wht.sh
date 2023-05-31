killall python3
echo
/bin/python3 ./Points.py &
echo "Appuyez sur Entrée pour lancer Image avec couleur"
read -n 1 -s key
if [ "$key" == "a" ]; then 
    ./script_wht.sh 
else
    killall python3
    echo
    /bin/python3 ./Image.py bleu.jpg rouge.webp  &
    read -n 1 -s -r -p "Appuyez sur Entrée pour lancer Image avec parthenon et space"
    echo
    killall python3
    /bin/python3 ./Image.py parthenon.jpg space.jpg &
    read -n 1 -s -r -p "Appuyez sur Entrée pour lancer Image avec couleur et Whitening"
    killall python3
    echo
    /bin/python3 ./ImageAvecWhitening.py bleu.jpg rouge.webp  &
    read -n 1 -s -r -p "Appuyez sur Entrée pour lancer Image avec parthenon et space et Whitening"
    echo
    killall python3
    /bin/python3 ./ImageAvecWhitening.py parthenon.jpg space.jpg &
    read -n 1 -s -r -p "Appuyez sur Entrée pour terminer"
    echo
    killall python3
    echo fin du test
fi

