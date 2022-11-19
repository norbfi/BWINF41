#! /bin/zsh

#input
echo "Bitte PFAD zu 'Alice_im_Wunderland.txt' eingeben"
read fname
echo "Bitte Satz zum Suchen eingeben (alles kleingeschrieben)"
read input
search="$(tr '[:lower:]' '[:upper:]' <<< ${input:0:1})${input:1}"

#change "_" in 
for (( i=0; i<${#search}; i++ )); do
    char=${search:$i:1};
    if [ $char = "_" ]; then
        search=${search/_/.*};
    fi
done
echo $search
echo $fname

#use grep, pattern = Das.*mir.*vor.*, fname = Alice_im_Wunderland.txt 
if [ -f $fname ]; then
    result=`grep -E "$search" $fname`
    echo $result;
fi