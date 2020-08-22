# E-Commerce Text Classification

Given a product title, classify the category the product belongs to.

## Installation
Installing the python service package (recommend to use virtualenv with python3.6)
```bash
cd service/
pip install -r requirement.txt
```
Installing npm serve
```bash
sudo npm install -g serve
```

## Usage

run Flask server
```bash
cd service/
FLASK_APP=app.py flask run
```
run npm serve
```bash
cd ui/
sudo npm run build
sudo serve -s build -l 3000
```
## References
More info regarding the webapp template: 
[Link](https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33)

More info regarding npm and React:
[Link](ui/README.md)

## License
[Apache 2.0](LICENSE)
