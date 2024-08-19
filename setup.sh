#!/bin/bash

DIR=`dirname "$0"`

echo ""
echo "====================="
echo "Installationsprogramm"
echo "====================="

echo ""
echo "Überprüfe die Verfügbarkeit von Python3 ..."
if ! command -v python3 &> /dev/null
then
    echo " ⛔ python3 wurde nicht gefunden. Bitte installieren und erneut versuchen!"
    exit 1
else
    echo " ✅ python3 wurde gefunden."
fi

echo ""
echo "Installiere virtuelle Python-Umgebung ..."
echo " 💡 mkdir $DIR/venv"
mkdir -p $DIR/venv
if [ $? != 0 ]; then
    echo ""
    echo "⛔ Installation abgebrochen!"
    exit 1
fi
echo " 🏗️  python3 -m venv $DIR/venv/"
python3 -m venv $DIR/venv/
if [ $? != 0 ]; then
    echo ""
    echo "⛔ Installation abgebrochen!"
    exit 1
fi

echo ""
echo "Installiere Python-Bibliotheken ..."
pip="$DIR/venv/bin/pip"
if [ ! -f "$pip" ]; then
    pip="$DIR/venv/Scripts/pip3.exe"
fi
echo " 📦 $pip install -r $DIR/requirements.txt"
$pip install -r $DIR/requirements.txt
if [ $? != 0 ]; then
    echo ""
    echo "⛔ Installation abgebrochen!"
    exit 1
fi

echo ""
echo "🚀 Installation abgeschlossen."
exit 0