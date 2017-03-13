
    export ROMS=( " " "AICP" "AOKP" "AOSiP" "AOSP-CAF" "AOSP-OMS" "BlissRoms" \
        "CandyRoms" "CarbonROM" "crDroid" "Cyanide" "CyanogenMod" "DirtyUnicorns" \
        "Euphoria" "F-AOSP" "FlayrOS" "Krexus" "Lineage Android" "OctOs" \
        "OmniROM" "OrionOS" "OwnROM" "PAC ROM" "Parallax OS" "Paranoid Android"\
        "Resurrection Remix" "SlimRoms" "Temasek" "GZR Tesla" "TipsyOs" \
        "GZR Validus" "VanirAOSP" "XenonHD" "XOSP" "Zephyr-OS" "AOSiP" "ABC ROM" \
        "DirtyUnicorns" "Krexus" "Nitrogen OS" "PureNexus" );
    echo -e "\n${CL_WYT}=======================================================${NONE}\n";
    echo -e "${CL_YEL}[?]${NONE} ${CL_WYT}Which ROM are you trying to build\nChoose among these (Number Selection)\n";
    for CT in {1..34}; do
        echo -e "${CT}. ${ROMS[$CT]}";
    done | pr -t -2
    echo -e "\n${INF} ${CL_WYT}Non-CAF / Nexus-Family ROMs${NONE}";
    echo -e "${INF} ${CL_WYT}Choose among these ONLY if you're building for a Nexus Device\n"
    for CT in {35..40}; do
        echo -e "${CT}. ${ROMS[$CT]}";
    done | pr -t -2
    unset CT CNS SBRN; # Unset these
    echo -e "\n=======================================================${NONE}\n";
    [ -z "$automate" ] && prompt SBRN;
    rom_names "$SBRN";
    if [[ "${SBRN}" == "Invalid" ]]; then
        echo -e "\n${LRED}Invalid Selection.${NONE} Going back."; rom_select;
    else
        echo -e "\n${INF} You have chosen -> ${ROM_FN}\n";
    fi
