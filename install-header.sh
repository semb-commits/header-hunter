#!/bash
echo "[+] Install dependensi..."
pkg install python -y
pip install requests colorama

echo "[+] Download script..."
curl -s https://raw.githubusercontent.com/semb-commits/header-hunter/main/header.py -o header.py

echo "[+] Selesai! Jalanin dengan: python header.py"
