# using httpie
# cat requests.txt | grep <request># | cut -d'#' -f3 | xargs http

IFS='|'

if [ "x$1" == "x-l" ]; then
    cat requests.txt | grep -P '^R\d+' | cut -d'#' -f2
else
    ARG=$@
    REQ=$(cat requests.txt | grep "${ARG}" | cut -d'#' -f3)
    sh -c $REQ
fi
