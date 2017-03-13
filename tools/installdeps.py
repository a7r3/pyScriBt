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
