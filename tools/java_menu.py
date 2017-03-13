    {
        echo -e "\n${CL_WYT}========${NONE} ${CL_YEL}JAVA${NONE} Installation ${CL_WYT}=======${NONE}\n";
        echo -e "1. Install Java";
        echo -e "2. Switch Between Java Versions / Providers\n";
        echo -e "0. Quick Menu\n";
        echo -e "${INF} ScriBt installs Java by OpenJDK";
        echo -e "\n${CL_WYT}=======================================================\n${NONE}";
        prompt JAVAS;
        case "$JAVAS" in
            0)  quick_menu ;;
            1)
                echo -ne '\033]0;ScriBt : Java\007';
                echo -e "\n${QN} Android Version of the ROM you're building";
                echo -e "1. Java 1.6.0 (4.4.x Kitkat)";
                echo -e "2. Java 1.7.0 (5.x.x Lollipop && 6.x.x Marshmallow)";
                echo -e "3. Java 1.8.0 (7.x.x Nougat)\n";
                [[ "${PKGMGR}" == "apt" ]] && echo -e "4. Ubuntu 16.04 & Want to install Java 7\n5. Ubuntu 14.04 & Want to install Java 8\n";
                prompt JAVER;
                case "$JAVER" in
                    1) java_install 6 ;;
                    2) java_install 7 ;;
                    3) java_install 8 ;;
                    4) java_ppa 7 ;;
                    5) java_ppa 8 ;;
                    *)
                        echo -e "\n${FLD} Invalid Selection.\n";
                        java_menu;
                        ;;
                esac # JAVER
                ;;
            2) java_select ;;
            *)
                echo -e "\n${FLD} Invalid Selection.\n";
                java_menu;
                ;;
        esac # JAVAS
