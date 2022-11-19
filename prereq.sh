pip install gdown
pip install plotly
pip install pandas
pip install numpy
pip install scipy
pip install scikit-learn
pip install morfessor
pip install bpemb

gdown --id 1UHbNavBR7ODDBwn5TytKurFzSxP_W6Ly -O ./toy_data/ma/

cd code
./run.sh ma charn add 0.05 10000

cd ../toy_data/bpe
python3 bpe

cd ..
morfessor -t ma.sent.1m.5.word -o ./ma.sent.1m.5.morf -s ./ma.sent.1m.5.morf.model
cd morf
python3 morf-format.py
