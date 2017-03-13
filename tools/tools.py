
    # change terminal title
    [ ! -z "$automate" ] && teh_action 5;

    function installdeps()
    {
        echo -e "\n${EXE} Analyzing Distro";
        for REL in lsb-release os-release debian-release; do
            if [ -f "/etc/${REL}" ]; then
                source /etc/${REL};
                case "$REL" in
                    "lsb-release") DID="${DISTRIB_ID}"; VER="${DISTRIB_RELEASE}" ;;
                    "os-release") DID="${ID}"; VER="${VERSION_ID}" ;; # Most of the Newer Distros
                    "debian-release") DID="debian" VER=`cat /etc/debian-release` ;;
#                   "other-release") DID="Distro Name (Single Worded)"; VER="Version (Single numbered)" ;;
                esac
            fi
        done
        dist_db "$DID" "$VER"; # Determination of Distro by a Database
        [[ ! -z "$DID"  && ! -z "$VER" ]] && \
        echo -e "\n${SCS} Distro Detected Successfully" || \
        (echo -e "\n${FLD} Distro not present in supported Distros\n\n${INF} Contact the Developer for Support\n"; quick_menu);

        echo -e "\n${EXE} Installing Build Dependencies\n";
        # Common Packages
        COMMON_PKGS=( git-core git gnupg flex bison gperf build-essential zip curl \
        libxml2-utils xsltproc g++-multilib squashfs-tools zlib1g-dev \
        pngcrush schedtool python lib32z1-dev lib32z-dev lib32z1 \
        libxml2 optipng python-networkx python-markdown make unzip );
        case "$DYR" in
            D12)
                DISTRO_PKGS=( libc6-dev libncurses5-dev:i386 x11proto-core-dev \
                libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 \
                libgl1-mesa-dev libwxgtk2.8-dev mingw32 tofrodos zlib1g-dev:i386 ) ;;
            D13)
                DISTRO_PKGS=( zlib1g-dev:i386 libc6-dev lib32ncurses5 \
                lib32bz2-1.0 lib32ncurses5-dev x11proto-core-dev \
                libx11-dev:i386 libreadline6-dev:i386 \
                libgl1-mesa-glx:i386 libgl1-mesa-dev libwxgtk2.8-dev \
                mingw32 tofrodos readline-common libreadline6-dev libreadline6 \
                lib32readline-gplv2-dev libncurses5-dev lib32readline5 \
                lib32readline6 libreadline-dev libreadline6-dev:i386 \
                libreadline6:i386 bzip2 libbz2-dev libbz2-1.0 libghc-bzlib-dev \
                lib32bz2-dev libsdl1.2-dev libesd0-dev ) ;;
            D14)
                DISTRO_PKGS=( libc6-dev-i386 lib32ncurses5-dev liblz4-tool \
                x11proto-core-dev libx11-dev libgl1-mesa-dev maven maven2 libwxgtk2.8-dev) ;;
            D15)
                DISTRO_PKGS=( libesd0-dev liblz4-tool libncurses5-dev \
                libsdl1.2-dev libwxgtk2.8-dev lzop maven maven2 \
                lib32ncurses5-dev lib32readline6-dev liblz4-tool ) ;;
            D16)
                DISTRO_PKGS=( automake lzop libesd0-dev maven \
                liblz4-tool libncurses5-dev libsdl1.2-dev libwxgtk3.0-dev \
                lzop lib32ncurses5-dev lib32readline6-dev lib32z1-dev \
                libbz2-dev libbz2-1.0 libghc-bzlib-dev ) ;;
        esac
        # Install 'em all
        execroot apt-get install -y ${COMMON_PKGS[*]} ${DISTRO_PKGS[*]};
    } # installdeps

    function installdeps_arch()
    {
        # common packages
        PKGS="git gnupg flex bison gperf sdl wxgtk squashfs-tools curl ncurses zlib schedtool perl-switch zip unzip libxslt python2-virtualenv bc rsync maven";
        PKGS64="$( pacman -Sgq multilib-devel ) lib32-zlib lib32-ncurses lib32-readline";
        PKGSJAVA="jdk6 jdk7-openjdk";
        PKGS_CONFLICT="gcc gcc-libs";
        # sort out already installed pkgs
        for item in ${PKGS} ${PKGS64} ${PKGSJAVA}; do
            if ! pacman -Qq ${item} &> /dev/null; then
                PKGSREQ="${item} ${PKGSREQ}";
            fi
        done
        # if there are required packages, run the installer
        if [ ${#PKGSREQ} -ge 4 ]; then
            # choose an AUR package manager instead of pacman
            for item in yaourt pacaur packer; do
                if which ${item} &> /dev/null; then
                    AURMGR="${item}";
                fi
            done
            if [ -z ${AURMGR} ]; then
                echo -e "\n${FLD} no AUR manager found\n";
                exitScriBt 1;
            fi
            # look for conflicting packages and uninstall them
            for item in ${PKGS_CONFLICT}; do
                if pacman -Qq ${item} &> /dev/null; then
                    execroot pacman -Rddns --noconfirm ${item};
                    sleep 3;
                fi
            done
            # install required packages
            for item in ${PKGSREQ}; do
                ${AURMGR} -S --noconfirm $item;
            done
        else
            echo -e "\n${SCS} You already have all required packages\n";
        fi
    } # installdeps_arch

    function java_select()
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
    } # java_select

    function java_check()
    {
      if [[ $( java -version &> $TMP; grep -c "version \"1.$1" $TMP ) == "1" ]]; then
          echo -e "\n${CL_WYT}=======================================================${NONE}";
          echo -e "${SCS} OpenJDK-$1 or Java 1.$1.0 has been successfully installed";
          echo -e "${CL_WYT}=======================================================${NONE}";
      fi
    } # java_check

    function java_install()
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
    } # java_install

    function java_ppa()
    {
        if [[ ! $(which add-apt-repository) ]]; then
            echo -e "${EXE} add-apt-repository not present. Installing it";
            execroot apt-get install software-properties-common;
        fi
        execroot add-apt-repository ppa:openjdk-r/ppa -y; # Add Java PPA
        execroot apt-get update -y; # Update Sources
        execroot apt-get install openjdk-$1-jdk -y; # Install eet
        java_check $1;
    } # java_ppa

    function java_menu()
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
    } # java_menu

    function udev_rules()
    {
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
        echo -e "${EXE} Updating / Creating Android USB udev rules (51-android)\n";
        execroot curl -s --create-dirs -L -o /etc/udev/rules.d/51-android.rules -O -L https://raw.githubusercontent.com/snowdream/51-android/master/51-android.rules;
        execroot chmod a+r /etc/udev/rules.d/51-android.rules;
        execroot service udev restart;
        echo -e "\n${SCS} Done";
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
    } # udev_rules


    function git_creds()
    {
        echo -e "\n${INF} Enter the Details with reference to your ${CL_WYT}GitHub account${NONE}\n\n";
        sleep 2;
        echo -e "${QN} Enter the Username";
        echo -e "${INF} Username is the one which appears on the GitHub Account URL\n${INF} Ex. https://github.com/[ACCOUNT_NAME]\n";
        prompt GIT_U;
        echo -e "\n${QN} Enter the E-mail ID\n";
        prompt GIT_E;
        git config --global user.name "${GIT_U}";
        git config --global user.email "${GIT_E}";
        echo -e "\n${SCS} Done.\n"
        quick_menu;
    } # git_creds

    function check_utils_version()
    {
        # If util is repo then concatenate the file else execute it as a binary
        [[ "$1" == "repo" ]] && CAT="cat " || unset CAT;
        case "$2" in
            "utils") BIN="${CAT}utils/$1" ;; # Util Version that ScriBt has under utils folder
            "installed") BIN="${CAT}$(which $1)" ;; # Util Version that has been installed in the System
        esac
        case "$1" in # Installed Version
            "ccache") VER=`${BIN} --version | head -1 | awk '{print $3}'` ;;
            "make") VER=`${BIN} -v | head -1 | awk '{print $3}'` ;;
            "ninja") VER=`${BIN} --version` ;;
            # since repo is a python script and not a binary
            "repo") VER=`${BIN} | grep -m 1 VERSION |\
                        awk -F "= " '{print $2}' |\
                        sed -e 's/[()]//g' |\
                        awk -F ", " '{print $1"."$2}'`;
                    ;;
        esac
    } # check_utils_version

    function installer()
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
    } # installer

    function scribtofy()
    {
        echo -e "\n${INF} This Function allows ScriBt to be executed under any directory";
        echo -e "${INF} Temporary Files would be present at working directory itself";
        echo -e "${INF} Older ScriBtofications, if present, would be overwritten";
        echo -e "\n${QN} Shall I ScriBtofy ${CL_WYT}[y/n]${NONE}\n";
        prompt SBFY;
        case "$SBFY" in
            [Yy])
                    echo -e "\n${EXE} Adding ScriBt to PATH";
                    echo -e "# ScriBtofy\nexport PATH=\"${CALL_ME_ROOT}:\$PATH\";" > ${HOME}/.scribt;
                    [[ $(grep 'source ${HOME}/.scribt' ${HOME}/.bashrc) ]] && echo -e "\n#ScriBtofy\nsource \${HOME}/.scribt;" >> ${HOME}/.bashrc;
                    echo -e "\n${EXE} Executing ~/.bashrc";
                    source ~/.bashrc;
                    echo -e "\n${SCS} Done\n\n${INF} Now you can ${CL_WYT}bash ROM.sh${NONE} under any directory";
                ;;
            [Nn])
                echo -e "${FLD} ScriBtofication cancelled";
                ;;
        esac
    } # scribtofy

    function tool_menu()
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
    } # tool_menu

    tool_menu;
