    {
        echo -e "${INF} If you have Installed Multiple Versions of Java or Installed Java from Different Providers (OpenJDK / Oracle)";
        echo -e "${INF} You may now select the Version of Java which is to be used BY-DEFAULT\n";
        echo -e "${CL_WYT}=======================================================${NONE}\n";
        case "${PKGMGR}" in
            "apt")
                execroot update-alternatives --config java;
                echo -e "\n${CL_WYT}=======================================================${NONE}\n";
                execroot update-alternatives --config javac;
                ;;
            "pacman")
                archlinux-java status;
                echo -e "${QN} Please enter desired version (eg. \"java-7-openjdk\")\n";
                prompt ARCHJA;
                execroot archlinux-java set ${ARCHJA};
                ;;
        esac
        echo -e "\n${CL_WYT}=======================================================${NONE}";
