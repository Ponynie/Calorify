# Calorify: A Food Image Classification App

Calorify is a Streamlit application that uses a PyTorch model to classify images of food. The application takes an image as input and predicts the type of food in the image.

## Installation

This project requires Python 3.7 or higher and the following packages: Streamlit, PIL, and PyTorch. You can install the required packages by running:
```bash
pip install -r requirements.txt
```

## Usage

The main script in this project is `app.py`. It contains a function `load_model()` which loads a PyTorch model from a file named `model.pt`, and a `main()` function which runs the Streamlit application.

To run the application, use the following command:
```bash
streamlit run app.py
```
Once the application is running, you can upload an image of food using the file uploader. The application will then classify the image and display the predicted type of food.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
