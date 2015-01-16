if [ $1 = 'on' ] ; then
	echo "Turning monitor on"
	sudo tvservice -p;
	sudo chvt 6;
	sudo chvt 7
fi

if [ $1 = 'off' ] ; then
	echo "Turning monitor off"
	sudo tvservice -o
fi
