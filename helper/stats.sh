cd /Users/jtim/Dropbox/Academic/Sources/bahai-corpus/data/bahaullah/text
total_bahaullah=$(ls -l *.txt | wc -l)
bahaullah_words=$(find . -type f -print0 | xargs -0 cat | wc -w)
bahaullah_arabic=$(find *ar.txt -type f -print0 | xargs -0 cat | wc -w)
bahaullah_persian=$(find *fa.txt -type f -print0 | xargs -0 cat | wc -w)

cd /Users/jtim/Dropbox/Academic/Sources/bahai-corpus/data/abdulbaha/text
total_abdulbaha=$(ls -l *.txt | wc -l)
abdulbaha_words=$(find . -type f -print0 | xargs -0 cat | wc -w)
abdulbaha_arabic=$(find *ar.txt -type f -print0 | xargs -0 cat | wc -w)
abdulbaha_persian=$(find *fa.txt -type f -print0 | xargs -0 cat | wc -w)

total_works=$((total_bahaullah + total_abdulbaha))
total_words=$((bahaullah_words + abdulbaha_words))
total_arabic=$((bahaullah_arabic + abdulbaha_arabic))
total_persian=$((bahaullah_persian + abdulbaha_persian))

printf "\n"

echo "total tablets: "$total_works

printf "\n"

echo "total words of Bahá'u'lláh: "$bahaullah_words
echo "total words of \`Abdu'l-Bahá: "$abdulbaha_words
echo "total words: "$total_words

printf "\n"

echo "total Persian words: "$total_persian
echo "total Arabic words: "$total_arabic