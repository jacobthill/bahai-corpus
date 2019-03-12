#!/bin/bash
chmod u+x stats.sh

cd /Users/jtim/Dropbox/Academic/Sources/bahai-corpus/data/bahaullah/text
total_bahaullah=$(ls -l *.txt | wc -l)
bahaullah_persian=$(ls -l *fa.txt | wc -l)
bahaullah_arabic=$(ls -l *ar.txt | wc -l)
bahaullah_words=$(find . -type f -print0 | xargs -0 cat | wc -w)

cd /Users/jtim/Dropbox/Academic/Sources/bahai-corpus/data/abdulbaha/text
total_abdulbaha=$(ls -l *.txt | wc -l)
abdulbaha_persian=$(find . -type f -print0 | xargs -0 cat | wc -w)
abdulbaha_arabic=$(ls -l *ar.txt | wc -l)
abdulbaha_words=$(find . -type f -print0 | xargs -0 cat | wc -w)

total_works=$((total_bahaullah + total_abdulbaha))
total_words=$((bahaullah_words + abdulbaha_words))
total_arabic=$((bahaullah_arabic + abdulbaha_arabic))
total_persian=$((bahaullah_persina + abdulbaha_persian))

printf "\n"

echo "total tablets of Bahá'u'lláh: "$total_bahaullah
echo "total tablets of \`Abdu'l-Bahá: "$total_abdulbaha
echo "total tablets: "$total_works

printf "\n"

echo "total words of Bahá'u'lláh: "$bahaullah_words
echo "total words of \`Abdu'l-Bahá: "$abdulbaha_words
echo "total words: "$total_words

printf "\n"

echo "total Persian words: "$total_persian
echo "total Arabic word: "$total_arabic

