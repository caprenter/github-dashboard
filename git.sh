rm -rf out
mkdir out
./fetch_data.sh &> fetch_data.log || exit 1
python make_html.py || exit 1
cp favicon.png out/
mv web web.1
mv out web
rm -rf web.1
