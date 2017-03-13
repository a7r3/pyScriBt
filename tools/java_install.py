    {
        echo -ne "\033]0;ScriBt : Java $1\007";
        echo -e "\n${EXE} Installing OpenJDK-$1 (Java 1.$1.0)";
        echo -e "\n${INF} Remove other Versions of Java ${CL_WYT}[y/n]${NONE}? : \n";
        prompt REMOJA;
        echo;
        case "$REMOJA" in
            [yY])
                case "${PKGMGR}" in
                    "apt") execroot apt-get purge openjdk-* icedtea-* icedtea6-* ;;
                    "pacman") execroot pacman -Rddns $( pacman -Qqs ^jdk ) ;;
                esac
                echo -e "\n${SCS} Removed Other Versions successfully"
                ;;
            [nN]) echo -e "${EXE} Keeping them Intact" ;;
            *)
                echo -e "${FLD} Invalid Selection.\n";
                java_install $1;
                ;;
        esac
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
        case "${PKGMGR}" in
            "apt") execroot apt-get update -y ;;
            "pacman") execroot pacman -Sy ;;
        esac
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
        case "${PKGMGR}" in
            "apt") execroot apt-get install openjdk-$1-jdk -y ;;
            "pacman") execroot pacman -S jdk$1-openjdk ;;
        esac
        java_check $1;
