        {
            # Execute these before building kernel
            [ -z "${action_kinit}" ] && kinit;
            [ -z "${KCCP}" ] && settc;
            [ -z "${action_kcl}" ] && kclean;
            [ ! -z "${SBCUH}" ] && custuserhost;

            echo -e "\n${EXE} Compiling the Kernel\n";
            export ARCH="${SBKA}" CROSS_COMPILE="${SBKTL}/bin/${KCCP}";
            [ ! -z "$SBNT" ] && SBNT="-j${SBNT}";
            make ${SBKD};
            make ${SBNT} && echo -e "\n${SCS} Compiled Successfully\n" || echo -e "${FLD} Compilation failed\n";
            [ -z "$automate" ] && kbuild;
