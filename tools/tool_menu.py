    {
        echo -e "\n${CL_WYT}=======================${NONE} ${CL_LBL}Tools${NONE} ${CL_WYT}=========================${NONE}\n";
        echo -e "         1. Install Build Dependencies\n";
        echo -e "         2. Install Java (OpenJDK 6/7/8)";
        echo -e "         3. Setup ccache (After installing it)";
        echo -e "         4. Install/Update ADB udev rules";
        echo -e "         5. Add/Update Git Credentials${CL_WYT}*${NONE}";
        echo -e "         6. Install make ${CL_WYT}~${NONE}";
        echo -e "         7. Install ninja ${CL_WYT}~${NONE}";
        echo -e "         8. Install ccache ${CL_WYT}~${NONE}";
        echo -e "         9. Install repo ${CL_WYT}~${NONE}";
        echo -e "        10. Add ScriBt to PATH";
# TODO: echo -e "         X. Find an Android Module's Directory";
        echo -e "\n         0. Quick Menu";
        echo -e "\n${CL_WYT}*${NONE} Create a GitHub account before using this option";
        echo -e "${CL_WYT}~${NONE} These versions are recommended to use...\n...If you have any issue in higher versions";
        echo -e "${CL_WYT}=======================================================${NONE}\n";
        prompt TOOL;
        case "$TOOL" in
            0) quick_menu ;;
            1) case "${PKGMGR}" in
                   "apt") installdeps ;;
                   "pacman") installdeps_arch ;;
               esac
               ;;
            2) java_menu ;;
            3) set_ccvars ;;
            4) udev_rules ;;
            5) git_creds ;;
            6) installer "make" ;;
            7) installer "ninja" ;;
            8) installer "ccache" ;;
            9) installer "repo" ;;
            10) scribtofy ;;
# TODO:     X) find_mod ;;
            *) echo -e "${FLD} Invalid Selection.\n"; tool_menu ;;
        esac
        [ -z "$automate" ] && quick_menu;
