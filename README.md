# S20-team5-project

## Demo

[Video Demo](https://youtu.be/GEyq74H7NNE?t=363)

Firstly, clone the repository via `git clone https://github.com/CSCI4850/S20-team5-project` on the command line or by downloading the zip file from the root page of this repository.
This will give you access to all of the necessary files on your local machine.

The demo file for this project is [YahooFinance/yfinance-predict.ipynb](YahooFinance/yfinance-predict.ipynb).
This should be opened in Jupyter Lab.
If Jupyter Lab is installed on your system, it can be launched via `jupyter lab` from the root directory of your local copy of the repository.
Otherwise, follow instructions elsewhere to install Jupyter Lab or use some other means of accessing IPython Notebooks.

A small amount of text is included at the top of the demo file explaining what it is: a simple feed-forward network capable of teasing apart the chaos of a set of time-series stock data and predicting the next day future price.
The first few code blocks set up the required imports for the project to run.
If you don't have these available, you can typically install them easily via `pip3 install <what-was-missing>` (note on some systems this will need to be `pip` rather than `pip3`, but python3 is the language these files were constructed with).

The first few blocks of code just demo the basics of how we fetch stock data.
An example is given to show fetching all the available Apple stock data.
To fetch this data, you need the "ticker name" for the requested stock (for Apple, this is `AAPL`).
The `period='max'` part is what fetches all the data.
These parameters can be changed to fetch different types of data (default is daily).
Refer to the [yfinance github readme](https://github.com/ranaroussi/yfinance) for examples of some of the other types of data fetches you can perform.

The next code block establishes the list of ticker names that will be fetched.
Eight (8) are included in the demo file, but feel free to add or remove content (must have at least 1).
The next few blocks fetch the data, construct the time series data, and normalize it to prepare for learning.

The code block starting with `model = ...` is the actual neural network model that is being constructed with the keras framework.
For the short demo, the number of neurons is kept relatively small and there is only one hidden layer with ReLU units.
Feel free to add/remove layers or change the number of neurons or activations (note, for networks with many layers it is recommended to use the `relu` activation, as the demo does).
The `Flatten` layer is more of a convenience that allows you to add more advanced layers like convolutions prior to it (it maintains the physical structure prior to that point, then just changes to a dense unstructured input for the following layers).
This is somewhat typical as the last step of convolutional networks.

The line immediately after this trains the network on the generated (and normalized) time series data.
For time's sake the number of epochs (effectively, learning time) is set low at 60.
For the video guide, 600 were used to give better performance.
Try using low numbers initially to see how long it takes to finish processing before increasing it.

The next two blocks show the results of learning.
The first plots the accuracy and loss of the net with respect to epochs (time, essentially).
The accuracy value on a regression problem such as this is not incredibly meaningful, as keras is just trying to create a percentage accuracy for a regression problem even though that's not strictly-speaking a real statistical measure that has much meaning.
The more important value is the second (bottom) graph of the loss function.
Assuming you left the default loss function in the model, this is the Mean Squared Error (MSE), which is a statistical measure you might use in regression analysis to say how well some approximation fits some data.
Zero means it fit the data perfectly, so lower is better (it will never by negative).

The next (final) code block grabs the most recent (chronologically-last) training window and shows the expected value andthe predicted value.
For a sufficiently good network that has been trained long enough, the predicted values should approach the expected.
The values themselves are overall multiples of the first point in the input window (so basically percentage increase).
This gives you insight into how well the network is performing on any individual stock as opposed to the MSE analysis for all stocks in the 8-dimensional output space (due to the fact that we predict values for all stocks simultaneously).
