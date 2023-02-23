from app import app ## import app dari package app yang kita buat

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])