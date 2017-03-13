    {
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
        echo -e "${EXE} Updating / Creating Android USB udev rules (51-android)\n";
        execroot curl -s --create-dirs -L -o /etc/udev/rules.d/51-android.rules -O -L https://raw.githubusercontent.com/snowdream/51-android/master/51-android.rules;
        execroot chmod a+r /etc/udev/rules.d/51-android.rules;
        execroot service udev restart;
        echo -e "\n${SCS} Done";
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
