# Challenge 2

## Approach problem summary

My initial thoughts in solving this problem is to try to solve it by applying one of the common methods of smoothing: Savitzky-Golay filter. 

## Installation

* The script can run on any OS(Windows, MacOS, Linux, etc.) with Python 3.* installed.

### Install dependencies

```bash
pip install numpy
pip install math
pip install random
pip install matplotlib
```

## Usage

```bash
cd ~/worktest/challenge_2
chmod +x preprocess_coordinates.py
python preprocess_coordinates.py
```

## Details about the implementation

- Generates points of a circle with specified radius with noise for the 'x' and 'y' coordinates.
- Injects a number of specified outliers.
- Uses the savgol_filter from scipy.signal.

## License
[MIT](https://choosealicense.com/licenses/mit/)