echo "Hello World..." > work/out.txt

pushd work

if [ ! -d "CapsNet-Tensorflow" ]; then
  apt-get update
  apt-get install git -y
  git clone https://github.com/naturomics/CapsNet-Tensorflow.git
fi

mkdir -p CapsNet-Tensorflow/data/mnist
python ../download_mnist.py
bash ../unzip_data.sh

pip install tqdm
python CapsNet-Tensorflow/main.py

popd

echo "and Goodnight!" >> work/out.txt
