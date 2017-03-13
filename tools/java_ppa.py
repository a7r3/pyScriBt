    {
        if [[ ! $(which add-apt-repository) ]]; then
            echo -e "${EXE} add-apt-repository not present. Installing it";
            execroot apt-get install software-properties-common;
        fi
        execroot add-apt-repository ppa:openjdk-r/ppa -y; # Add Java PPA
        execroot apt-get update -y; # Update Sources
        execroot apt-get install openjdk-$1-jdk -y; # Install eet
        java_check $1;
