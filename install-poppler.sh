apt install g++ autoconf libfontconfig1-dev pkg-config libjpeg-dev libopenjpeg-dev gnome-common libglib2.0-dev gtk-doc-tools libyelp-dev yelp-tools gobject-introspection libsecret-1-dev libnautilus-extension-dev -y

wget https://poppler.freedesktop.org/poppler-data-0.4.7.tar.gz

tar -xf poppler-data-0.4.7.tar.gz

cd poppler-data-0.4.7

make install

cd ..

wget https://poppler.freedesktop.org/poppler-0.48.0.tar.xz
tar -xf poppler-0.48.0.tar.xz
cd poppler-0.48.0

./configure

make

make install

ln -s /usr/local/bin/pdftotext /usr/bin/pdftotext
ln -s /usr/local/bin/pdftoppm /usr/bin/pdftoppm
ln -s /usr/local/lib/libpoppler.so.64 /usr/lib/libpoppler.so.64
