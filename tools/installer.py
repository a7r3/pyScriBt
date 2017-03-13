    {
        echo -e "\n${EXE}Checking presence of ~/bin folder\n";
        if [ -d ${HOME}/bin ]; then
            echo -e "${SCS} ${HOME}/bin present";
        else
            echo -e "${FLD} ${HOME}/bin absent\n${EXE} Creating folder ${HOME}/bin\n${EXE} `mkdir -pv ${HOME}/bin`";
        fi
        check_utils_version "$1" "utils"; # Check Binary Version by ScriBt
        echo -e "\n${EXE} Installing $1 $VER\n";
        echo -e "${QN} Do you want $1 to be Installed for";
        echo -e "\n1. This user only (${HOME}/bin)\n2. All users (/usr/bin)\n";
        prompt UIC; # utility installation choice
        case "$UIC" in
            1) IDIR="${HOME}/bin/" ;;
            2) IDIR="/usr/bin/" ;;
            *) echo -e "\n${FLD} Invalid Selection\n"; installer $@ ;;
        esac
        sudo -p $'\n\033[1;35m[#]\033[0m ' install utils/$1 ${IDIR};
        check_utils_version "$1" "installed"; # Check Installed Version
        echo -e "\n${INF} Installed Version of $1 : $VER";
        if [[ "$1" == "ninja" ]]; then
            echo -e "\n${INF} To make use of Host versions of Ninja, make sure the build repo contains the following change\n";
            echo -e "https://github.com/CyanogenMod/android_build/commit/e572919037726eff75fddd68c5f18668c6d24b30";
            echo -e "\n${INF} Cherry-Pick this commit under the ${CL_WYT}build${NONE} folder/repo of the ROM you're building";
        fi
        echo -e "\n${SCS} Done\n";
