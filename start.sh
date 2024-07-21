#!/bin/bash
echo "Start eingeleitet. VertretungsPlaner wird gestartet."
screen -dmS VertretungsPlaner bash -c "python3 main.py; screen -XS $STY quit"
while true; do
	if ! screen -ls | grep -q "VertretungsPlaner"; then
		echo "VertretungsPlaner ist gecrasht. Ich starte VertretungsPlaner neu."
		screen -dmS VertretungsPlaner bash -c "python3 main.py; screen -XS $STY quit"
	fi
	sleep 1
done