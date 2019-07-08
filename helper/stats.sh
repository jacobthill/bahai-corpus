cd /Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/bahaullah/text
total_bahaullah=$(ls -l *.txt | wc -l)
bahaullah_words=$(find . -type f -print0 | xargs -0 cat | wc -w)
bahaullah_arabic=$(find *ar.txt -type f -print0 | xargs -0 cat | wc -w)
bahaullah_persian=$(find *fa.txt -type f -print0 | xargs -0 cat | wc -w)

cd /Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/bab/text
total_bab=$(ls -l *.txt | wc -l)
bab_words=$(find . -type f -print0 | xargs -0 cat | wc -w)
bab_arabic=$(find *ar.txt -type f -print0 | xargs -0 cat | wc -w)
bab_persian=$(find *fa.txt -type f -print0 | xargs -0 cat | wc -w)

cd /Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/abdulbaha/text
total_abdulbaha=$(ls -l *.txt | wc -l)
abdulbaha_words=$(find . -type f -print0 | xargs -0 cat | wc -w)
abdulbaha_arabic=$(find *ar.txt -type f -print0 | xargs -0 cat | wc -w)
abdulbaha_persian=$(find *fa.txt -type f -print0 | xargs -0 cat | wc -w)

cd /Users/jtim/Dropbox/Academic/sources/corpora/bahai-corpus/data/shoghi-effendi/text
total_shoghi_effendi=$(ls -l *.txt | wc -l)
shoghi_effendi_words=$(find . -type f -print0 | xargs -0 cat | wc -w)
shoghi_effendi_arabic=$(find *ar.txt -type f -print0 | xargs -0 cat | wc -w)
shoghi_effendi_persian=$(find *fa.txt -type f -print0 | xargs -0 cat | wc -w)

total_works=$((total_bahaullah + total_bab + total_abdulbaha + total_shoghi_effendi))
total_words=$((bahaullah_words + bab_words + abdulbaha_words + shoghi_effendi_words))
total_arabic=$((bahaullah_arabic + bab_arabic + abdulbaha_arabic + shoghi_effendi_arabic))
total_persian=$((bahaullah_persian + bab_persian + abdulbaha_persian + shoghi_effendi_persian))

printf "\n"

echo "total tablets of Bahá'u'lláh: "$total_bahaullah
echo "total tablets of the Báb: "$total_bab
echo "total tablets of \`Abdu'l-Bahá: "$total_abdulbaha
echo "total tablets of Shoghi Effendi "$total_shoghi_effendi
echo "total tablets: "$total_works

printf "\n"

echo "total words of Bahá'u'lláh: "$bahaullah_words
echo "total words of the Báb: "$bab_words
echo "total words of \`Abdu'l-Bahá: "$abdulbaha_words
echo "total words of Shoghi Effendi: "$shoghi_effendi_words
echo "total words: "$total_words

printf "\n"

echo "total Persian words: "$total_persian
echo "total Arabic words: "$total_arabic