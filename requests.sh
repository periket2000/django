# using httpie
# cat requests.txt | grep <request># | cut -d'#' -f3 | xargs http

IFS='|'

if [ "x$1" == "x-pr" ]; then
    DATA=$(curl -s https://random-data-api.com/api/restaurant/random_restaurant)
    TITLE=$(echo $DATA | jq '.name')
    DESC=$(echo $DATA | jq '.description')
    PAGES=10
    REQ=$(echo http --raw \'{\"title\": "$TITLE", \"description\": "$DESC", \"pages\": $PAGES}\' POST http://localhost:8000/api/pdfs/)
    sh -c $REQ
    exit 0
fi

if [ "x$1" == "x-g" ]; then
    VAL=$2
    REQ=$(echo http GET http://localhost:8000/api/pdfs/$VAL/)
    sh -c $REQ
    exit 0
fi

if [ "x$1" == "x-l" ]; then
    cat requests.txt | grep -P '^R\d+' | cut -d'#' -f2
else
    ARG=$@
    REQ=$(cat requests.txt | grep "${ARG}" | cut -d'#' -f3)
    sh -c $REQ
fi
