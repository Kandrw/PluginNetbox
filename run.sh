
cd netbox-docker

while getopts "crb" OPTION; do
    case $OPTION in
	c)
        docker compose build --no-cache
        exit;
    ;;
    r)
        docker-compose up -d
        exit;
    ;;
    b)
        docker-compose down
        exit;
    ;;
	*)
		echo "Incorrect option"
	;;
	esac
done

if [[ $OPTIND == 1 ]]; then

    echo "Not found command"
    echo "Build: ./run.sh -c"
    echo "Start: ./run.sh -r"
    echo "Stop: ./run.sh -d"
    
fi
