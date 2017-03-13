        {   # AOSP-CAF|RRO|F-AOSP|Flayr|OmniROM|Zephyr
            echo -e "${EXE} Adding Lunch Combo in Device Tree";
            [ ! -f vendorsetup.sh ] && touch vendorsetup.sh;
            if [[ $(grep -c "${ROMNIS}_${SBDEV}" ${DEVDIR}/vendorsetup.sh ) == "0" ]]; then
                echo -e "add_lunch_combo ${ROMNIS}_${SBDEV}-${SBBT}" >> vendorsetup.sh;
            else
                echo -e "${SCS} Lunch combo already added to vendorsetup.sh\n";
            fi
