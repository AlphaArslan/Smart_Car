sleep 10
sudo modprobe bcm2835-v4l2
cd /home/pi/Desktop/alpha/Smart_Car

echo "media script"
python3 media.py &

echo "camera script"
python3 camera.py >log/camera.txt 2>&1 &

echo "motor script"
python3 motor.py >log/motor.txt 2>&1 &

echo "line_auto script"
python3 line_auto.py >log/line_auto.txt 2>&1 &

echo "server script"
cd webpage
python3 server.py >../log/server.txt 2>&1 &

echo "done"
touch ~/Desktop/running
